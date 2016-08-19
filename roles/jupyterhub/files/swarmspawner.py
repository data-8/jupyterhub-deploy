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

    @gen.coroutine
    def lookup_node_name(self):
        """Find the name of the swarm node that the container is running on."""
        containers = yield self.docker('containers', all=True)
        for container in containers:
            if container['Id'] == self.container_id:
                name, = container['Names']
                node, container_name = name.lstrip("/").split("/")
                raise gen.Return(node)

    @gen.coroutine
    def start(self, image=None, extra_create_kwargs=None, extra_host_config=None):
        # look up mapping of node names to ip addresses
        info = yield self.docker('info')
        self.log.info('SystemStatus: ' + str(info['SystemStatus']))
        num_nodes = int(info['SystemStatus'][3][1])
        self.log.info('num_nodes: ' + str(num_nodes))
        node_info = info['SystemStatus'][4::9] # swarm 1.2.4; docker-py v1.7-1.8
        self.log.info('node_info: ' + str(node_info))
        self.node_info = {}
        for i in range(num_nodes):
            node, ip_port = node_info[i]
            if node == '':
                self.log.info('name for ip_port %s is empty.' % ip_port)
            self.node_info[node.strip()] = ip_port.split(":")[0]
        self.log.debug("Swarm nodes are: {}".format(self.node_info))

        # start the container
        self.log.info("starting container: image:{}".format(image))
        yield DockerSpawner.start(
            self, image=image, extra_create_kwargs=extra_create_kwargs,
            extra_host_config=extra_host_config)

        # figure out what the node is and then get its ip
        name = yield self.lookup_node_name()
        self.user.server.ip = self.node_info[name]
        self.log.info(self.env)
        self.log.info("api: {} started on {} ({}:{})".format(
            self.container_name, name, self.user.server.ip,
            self.user.server.port))

        # Future method of determining ip
        inspection = self.client.inspect_container(self.container_id)
        ip = inspection['Node']['IP']
        node = inspection['Node']['Name']
        container_name = inspection['Name'][1:] # omit leading "/"
        self.log.info("inspector: {} started on {} ({})".format(
            container_name, node, ip))
        # Register IP in ORM ; don't enable this yet
        #self.user.server.ip = ip
        #self.user.server.port = port
