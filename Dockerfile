FROM ubuntu:14.04

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -q -y ssh make python-dev
	
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN pip install ansible==1.9.3
RUN mkdir /etc/ansible
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts

ADD . /root/jupyterhub-deploy/

WORKDIR /root/jupyterhub-deploy/
