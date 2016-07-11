from tornado import gen
from dockerspawner import DockerSpawner, SystemUserSpawner

# urllib3 complains that we're making unverified HTTPS connections to swarm,
# but this is ok because we're connecting to swarm via 127.0.0.1. I don't
# actually want swarm listening on a public port, so I don't want to connect
# to swarm via the host's FQDN, which means we can't do fully verified HTTPS
# connections. To prevent the warning from appearing over and over and over
# again, I'm just disabling it for now.
import requests
requests.packages.urllib3.disable_warnings()


class SwarmSpawner(SystemUserSpawner):

    container_ip = '0.0.0.0'

    @gen.coroutine
    def start(self, image=None, extra_create_kwargs={}, extra_host_config={}):
        # specify extra host configuration
        if 'mem_limit' not in extra_host_config:
            extra_host_config['mem_limit'] = '2g'
        # specify extra creation options
        if 'working_dir' not in extra_create_kwargs:
            extra_create_kwargs['working_dir'] = self.homedir

        # start the container
        self.log.info("starting container")
        yield DockerSpawner.start(
            self, image=image, extra_create_kwargs=extra_create_kwargs,
            extra_host_config=extra_host_config)

        # Ask swarm about our container
        inspection = self.client.inspect_container(self.container_id)
        ip = inspection['Node']['IP']
        node = inspection['Node']['Name']
        container_name = inspection['Name'][1:] # omit leading "/"
        # Log
        self.log.info("{} started on {} ({})".format(container_name, node, ip))
        self.log.info(self.env)
        # Register IP in ORM
        self.user.server.ip = ip

    def _user_id_default(self):
        self.log.debug(self.user.state)
        return self.user.state['user_id']
