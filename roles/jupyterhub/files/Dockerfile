FROM jupyter/jupyterhub:1a4226419f0ecdceec98c26d8c4525cd3bb04b82

MAINTAINER Ryan Lovett <rylo@berkeley.edu>

# We need to update pip, otherwise the version of requests that
# is installed by dockerspawner breaks things.
RUN pip3 install --upgrade pip

# Install dockerspawner and oauthenticator
RUN /usr/local/bin/pip3 install git+git://github.com/docker/docker-py.git@1e916a1e83af49bc8d2fd5026ca9746129d1cebc
RUN /usr/local/bin/pip3 install git+git://github.com/jupyter/dockerspawner.git@c7a3f6d75adeaa67116ff237984c45af57e0fa93
RUN /usr/local/bin/pip3 install git+git://github.com/ryanlovett/jh-google-oauthenticator.git

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

#RUN sed -i -e 's/^<\/body>/&\n  <div><p style="padding:1em; position:absolute; left:0px; bottom:0px;">This computing environment is provided through the generous support of the Microsoft Azure platform and the Intel Corporation.<\/p><\/div>\n&/' /usr/local/share/jupyter/hub/templates/page.html

# set working directory to the jupyterhub directory
WORKDIR /srv/jupyterhub
