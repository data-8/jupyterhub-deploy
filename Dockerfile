FROM ansible/ubuntu14.04-ansible:stable

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -q -y ssh make

ADD . /root/jupyterhub-deploy/

WORKDIR /root/jupyterhub-deploy/
