FROM jupyterhub/jupyterhub-onbuild:0.6.1

MAINTAINER Ryan Lovett <rylo@berkeley.edu>

# 
RUN conda install ipython

# Install dockerspawner and oauthenticator
#RUN pip install git+git://github.com/jupyter/dockerspawner.git@c7a3f6d75adeaa67116ff237984c45af57e0fa93
#RUN pip install git+git://github.com/docker/docker-py.git@1e916a1e83af49bc8d2fd5026ca9746129d1cebc
RUN pip install git+git://github.com/docker/docker-py.git@1.8.1
RUN pip install git+git://github.com/jupyterhub/dockerspawner.git@0.4.0
RUN /opt/conda/bin/pip install oauthenticator==0.4.*

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

# set working directory to the jupyterhub directory
WORKDIR /srv/jupyterhub

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py", "--no-ssl"]
