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
  adduser -q --gecos "" testuser1 && \
  adduser -q --gecos "" testuser2 && \
  adduser -q --gecos "" testuser3 && \
  adduser -q --gecos "" testuser4 && \
  adduser -q --gecos "" testuser5 && \
  adduser -q --gecos "" testuser6 && \
  adduser -q --gecos "" testuser7 && \
  adduser -q --gecos "" testuser8 && \
  adduser -q --gecos "" testuser9 && \
  adduser -q --gecos "" testuser10 && \
  adduser -q --gecos "" testuser11 && \
  adduser -q --gecos "" testuser12 && \
  adduser -q --gecos "" testuser13 && \
  adduser -q --gecos "" testuser14 && \
  adduser -q --gecos "" testuser15 && \
  adduser -q --gecos "" testuser16 && \
  adduser -q --gecos "" testuser17 && \
  adduser -q --gecos "" testuser18 && \
  adduser -q --gecos "" testuser19 && \
  adduser -q --gecos "" testuser20 && \
  adduser -q --gecos "" testuser21 && \
  adduser -q --gecos "" testuser22 && \
  adduser -q --gecos "" testuser23 && \
  adduser -q --gecos "" testuser24 && \
  adduser -q --gecos "" testuser25 && \
  adduser -q --gecos "" testuser26 && \
  adduser -q --gecos "" testuser27 && \
  adduser -q --gecos "" testuser28 && \
  adduser -q --gecos "" testuser29 && \
  adduser -q --gecos "" testuser30 && \
  adduser -q --gecos "" testuser31 && \
  adduser -q --gecos "" testuser32 && \
  adduser -q --gecos "" testuser33 && \
  adduser -q --gecos "" testuser34 && \
  adduser -q --gecos "" testuser35 && \
  adduser -q --gecos "" testuser36 && \
  adduser -q --gecos "" testuser37 && \
  adduser -q --gecos "" testuser38 && \
  adduser -q --gecos "" testuser39 && \
  adduser -q --gecos "" testuser40 && \
  adduser -q --gecos "" testuser41 && \
  adduser -q --gecos "" testuser42 && \
  adduser -q --gecos "" testuser43 && \
  adduser -q --gecos "" testuser44 && \
  adduser -q --gecos "" testuser45 && \
  adduser -q --gecos "" testuser46 && \
  adduser -q --gecos "" testuser47 && \
  adduser -q --gecos "" testuser48 && \
  adduser -q --gecos "" testuser49 && \
  adduser -q --gecos "" testuser50 && \
  adduser -q --gecos "" testuser51 && \
  adduser -q --gecos "" testuser52 && \
  adduser -q --gecos "" testuser53 && \
  adduser -q --gecos "" testuser54 && \
  adduser -q --gecos "" testuser55 && \
  adduser -q --gecos "" testuser56 && \
  adduser -q --gecos "" testuser57 && \
  adduser -q --gecos "" testuser58 && \
  adduser -q --gecos "" testuser59 && \
  adduser -q --gecos "" testuser60 && \
  adduser -q --gecos "" testuser61 && \
  adduser -q --gecos "" testuser62 && \
  adduser -q --gecos "" testuser63 && \
  adduser -q --gecos "" testuser64 && \
  adduser -q --gecos "" testuser65 && \
  adduser -q --gecos "" testuser66 && \
  adduser -q --gecos "" testuser67 && \
  adduser -q --gecos "" testuser68 && \
  adduser -q --gecos "" testuser69 && \
  adduser -q --gecos "" testuser70 && \
  adduser -q --gecos "" testuser71 && \
  adduser -q --gecos "" testuser72 && \
  adduser -q --gecos "" testuser73 && \
  adduser -q --gecos "" testuser74 && \
  adduser -q --gecos "" testuser75 && \
  adduser -q --gecos "" testuser76 && \
  adduser -q --gecos "" testuser77 && \
  adduser -q --gecos "" testuser78 && \
  adduser -q --gecos "" testuser79 && \
  adduser -q --gecos "" testuser80 && \
  adduser -q --gecos "" testuser81 && \
  adduser -q --gecos "" testuser82 && \
  adduser -q --gecos "" testuser83 && \
  adduser -q --gecos "" testuser84 && \
  adduser -q --gecos "" testuser85 && \
  adduser -q --gecos "" testuser86 && \
  adduser -q --gecos "" testuser87 && \
  adduser -q --gecos "" testuser88 && \
  adduser -q --gecos "" testuser89 && \
  adduser -q --gecos "" testuser90 && \
  adduser -q --gecos "" testuser91 && \
  adduser -q --gecos "" testuser92 && \
  adduser -q --gecos "" testuser93 && \
  adduser -q --gecos "" testuser94 && \
  adduser -q --gecos "" testuser95 && \
  adduser -q --gecos "" testuser96 && \
  adduser -q --gecos "" testuser97 && \
  adduser -q --gecos "" testuser98 && \
  adduser -q --gecos "" testuser99 && \
  adduser -q --gecos "" testuser100


CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py", "--no-ssl"]
