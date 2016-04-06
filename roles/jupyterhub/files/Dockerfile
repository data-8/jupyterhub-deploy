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

# set working directory to the jupyterhub directory
WORKDIR /srv/jupyterhub

# Let in everyone without password
RUN sed -i -e '/pam_deny/s/^/#/' /etc/pam.d/common-auth

RUN adduser -q --gecos "" samlau95
# Hack to allow logging in as test users T______T
RUN adduser -q --gecos "" samz
RUN adduser -q --gecos "" testuser1
RUN adduser -q --gecos "" testuser2
RUN adduser -q --gecos "" testuser3
RUN adduser -q --gecos "" testuser4
RUN adduser -q --gecos "" testuser5
RUN adduser -q --gecos "" testuser6
RUN adduser -q --gecos "" testuser7
RUN adduser -q --gecos "" testuser8
RUN adduser -q --gecos "" testuser9
RUN adduser -q --gecos "" testuser10
RUN adduser -q --gecos "" testuser11
RUN adduser -q --gecos "" testuser12
RUN adduser -q --gecos "" testuser13
RUN adduser -q --gecos "" testuser14
RUN adduser -q --gecos "" testuser15
RUN adduser -q --gecos "" testuser16
RUN adduser -q --gecos "" testuser17
RUN adduser -q --gecos "" testuser18
RUN adduser -q --gecos "" testuser19
RUN adduser -q --gecos "" testuser20
RUN adduser -q --gecos "" testuser21
RUN adduser -q --gecos "" testuser22
RUN adduser -q --gecos "" testuser23
RUN adduser -q --gecos "" testuser24
RUN adduser -q --gecos "" testuser25
RUN adduser -q --gecos "" testuser26
RUN adduser -q --gecos "" testuser27
RUN adduser -q --gecos "" testuser28
RUN adduser -q --gecos "" testuser29
RUN adduser -q --gecos "" testuser30
RUN adduser -q --gecos "" testuser31
RUN adduser -q --gecos "" testuser32
RUN adduser -q --gecos "" testuser33
RUN adduser -q --gecos "" testuser34
RUN adduser -q --gecos "" testuser35
RUN adduser -q --gecos "" testuser36
RUN adduser -q --gecos "" testuser37
RUN adduser -q --gecos "" testuser38
RUN adduser -q --gecos "" testuser39
RUN adduser -q --gecos "" testuser40
RUN adduser -q --gecos "" testuser41
RUN adduser -q --gecos "" testuser42
RUN adduser -q --gecos "" testuser43
RUN adduser -q --gecos "" testuser44
RUN adduser -q --gecos "" testuser45
RUN adduser -q --gecos "" testuser46
RUN adduser -q --gecos "" testuser47
RUN adduser -q --gecos "" testuser48
RUN adduser -q --gecos "" testuser49
RUN adduser -q --gecos "" testuser50
RUN adduser -q --gecos "" testuser51
RUN adduser -q --gecos "" testuser52
RUN adduser -q --gecos "" testuser53
RUN adduser -q --gecos "" testuser54
RUN adduser -q --gecos "" testuser55
RUN adduser -q --gecos "" testuser56
RUN adduser -q --gecos "" testuser57
RUN adduser -q --gecos "" testuser58
RUN adduser -q --gecos "" testuser59
RUN adduser -q --gecos "" testuser60
RUN adduser -q --gecos "" testuser61
RUN adduser -q --gecos "" testuser62
RUN adduser -q --gecos "" testuser63
RUN adduser -q --gecos "" testuser64
RUN adduser -q --gecos "" testuser65
RUN adduser -q --gecos "" testuser66
RUN adduser -q --gecos "" testuser67
RUN adduser -q --gecos "" testuser68
RUN adduser -q --gecos "" testuser69
RUN adduser -q --gecos "" testuser70
RUN adduser -q --gecos "" testuser71
RUN adduser -q --gecos "" testuser72
RUN adduser -q --gecos "" testuser73
RUN adduser -q --gecos "" testuser74
RUN adduser -q --gecos "" testuser75
RUN adduser -q --gecos "" testuser76
RUN adduser -q --gecos "" testuser77
RUN adduser -q --gecos "" testuser78
RUN adduser -q --gecos "" testuser79
RUN adduser -q --gecos "" testuser80
RUN adduser -q --gecos "" testuser81
RUN adduser -q --gecos "" testuser82
RUN adduser -q --gecos "" testuser83
RUN adduser -q --gecos "" testuser84
RUN adduser -q --gecos "" testuser85
RUN adduser -q --gecos "" testuser86
RUN adduser -q --gecos "" testuser87
RUN adduser -q --gecos "" testuser88
RUN adduser -q --gecos "" testuser89
RUN adduser -q --gecos "" testuser90
RUN adduser -q --gecos "" testuser91
RUN adduser -q --gecos "" testuser92
RUN adduser -q --gecos "" testuser93
RUN adduser -q --gecos "" testuser94
RUN adduser -q --gecos "" testuser95
RUN adduser -q --gecos "" testuser96
RUN adduser -q --gecos "" testuser97
RUN adduser -q --gecos "" testuser98
RUN adduser -q --gecos "" testuser99
RUN adduser -q --gecos "" testuser100


CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py", "--no-ssl"]
