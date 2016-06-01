FROM jupyter/jupyterhub:0.5.0

MAINTAINER Ryan Lovett <rylo@berkeley.edu>

# We need to update pip, otherwise the version of requests that
# is installed by dockerspawner breaks things.
RUN pip install --upgrade pip

RUN conda install ipython

# Install dockerspawner and oauthenticator
RUN pip install git+git://github.com/docker/docker-py.git@1e916a1e83af49bc8d2fd5026ca9746129d1cebc
RUN pip install git+git://github.com/jupyter/dockerspawner.git@c7a3f6d75adeaa67116ff237984c45af57e0fa93
RUN pip install git+git://github.com/ryanlovett/jh-google-oauthenticator.git

# Add variable to allow connecting to the docker swarm
ENV DOCKER_HOST https://127.0.0.1:2376

# Create oauthenticator directory -- this is where we'll put the userlist later
RUN mkdir /srv/oauthenticator
ENV OAUTHENTICATOR_DIR /srv/oauthenticator
RUN chmod 700 /srv/oauthenticator

# add the userlist, spawner, and authenticator
ADD userlist /srv/oauthenticator/userlist
ADD swarmspawner.py /srv/oauthenticator/swarmspawner.py
ADD docker_oauth.py /srv/oauthenticator/docker_oauth.py

# Try to make sure CHP is the version with statsd
# TODO(sam): Change this to a version once an update to CHP gets pushed to npm
RUN npm install git+https://github.com/jupyter/configurable-http-proxy#1d24f8b1f7db0c1313bb329f804b042641082ba0 && rm -rf ~/.npm

# set working directory to the jupyterhub directory
WORKDIR /srv/jupyterhub

# Let in everyone without password
RUN sed -i -e '/pam_deny/s/^/#/' /etc/pam.d/common-auth

RUN adduser -q --gecos "" samlau95
# Hack to allow logging in as test users T______T
RUN adduser -q --gecos "" samz && \
  adduser -q --gecos "" testuser1


CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py", "--no-ssl"]
