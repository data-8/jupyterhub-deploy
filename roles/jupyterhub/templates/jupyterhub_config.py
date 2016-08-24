# Configuration file for Jupyter Hub
c = get_config()

import os
import sys

# Base configuration
c.JupyterHub.log_level = "INFO"
c.JupyterHub.db_url = 'sqlite:////srv/jupyterhub_db/jupyterhub.sqlite'
c.JupyterHub.proxy_check_interval = 30

# Configure the authenticator
c.JupyterHub.authenticator_class = 'docker_oauth.DockerOAuthenticator'
c.DockerOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
c.DockerOAuthenticator.create_system_users = True
c.Authenticator.admin_users = admin = set()
#c.Authenticator.whitelist = whitelist = set()
c.GoogleOAuthenticator.hosted_domain = 'berkeley.edu'
c.GoogleOAuthenticator.login_service = 'UC Berkeley'

# Configure the spawner
c.JupyterHub.spawner_class = 'systemuserspawner.SystemUserSpawner'
#c.JupyterHub.spawner_class = 'swarmspawner.SwarmSpawner'
c.SystemUserSpawner.container_image = 'data8/systemuser:nodrive'
c.DockerSpawner.tls_cert = '{{ docker_tls_path }}/cert.pem'
c.DockerSpawner.tls_key = '{{ docker_tls_path }}/key.pem'
c.DockerSpawner.remove_containers = True
c.DockerSpawner.read_only_volumes = {'/home/shared':'/home/shared'}
c.DockerSpawner.extra_host_config = {'mem_limit': '2g'}
c.DockerSpawner.container_ip = "0.0.0.0"
#c.Spawner.start_timeout = 300
#c.Spawner.http_timeout = 150

# Possibly prevent NFS locking issues with sqlite
# https://github.com/jupyter/dockerspawner/issues/46
c.HistoryManager.enabled = False

# The docker instances need access to the Hub, so the default loopback port
# doesn't work:
c.JupyterHub.hub_ip = '{{ servicenet_ip }}'

# Add users to the admin list, the whitelist, and also record their user ids
root = os.environ.get('OAUTHENTICATOR_DIR', os.path.dirname(__file__))
sys.path.insert(0, root)

with open(os.path.join(root, 'userlist')) as f:
    for line in f:
        if line.isspace(): continue
        parts = line.split()
        #whitelist.add(name)
        if len(parts) > 1 and parts[1] == 'admin':
            admin.add(parts[0])
