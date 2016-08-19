# vim:set ts=4 shiftwidth=4 noet:

DEPLOY_C="ds/deploy:2"

REBUILD_TAGS=rebuild-proxy rebuild-systemuser rebuild-jupyterhub rebuild-interact rebuild-cull rebuild-stats rebuild-swarm jupyterhub_host

RUN_CMD="/bin/bash"

ansible:
	curl -sO https://bootstrap.pypa.io/get-pip.py
	sudo python get-pip.py
	sudo pip install 'ansible<2'

docker:
	curl -so install-docker.sh https://get.docker.com
	sudo bash install-docker.sh
	sudo usermod -aG docker $(shell id -u -n)

vault-password:
	openssl rand -hex 32 > vault-password

assemble_certs:
	script/assemble_certs

root_logins:
	script/enable-root-logins

build: secrets.vault.yml inventory
	docker build -t $(DEPLOY_C) .

run:
	docker run -it \
		-v $$SSH_AUTH_SOCK:/root/agent.sock \
		--env SSH_AUTH_SOCK=/root/agent.sock \
		-v $(shell pwd):/root/jupyterhub-deploy:rw \
		-v $(shell pwd)/../.ssh:/root/.ssh \
		-v $(shell pwd)/../proxy-certs/:/root/jupyterhub-deploy/proxy-certs \
		-v $(shell pwd)/../certificates/:/root/jupyterhub-deploy/certificates \
		$(DEPLOY_C) $(RUN_CMD)

deploy:
	ansible-vault encrypt --vault-password-file vault-password secrets.vault.yml
	ansible-vault encrypt --vault-password-file vault-password users.vault.yml
	#script/assemble_certs
	script/deploy

retry:
	script/deploy --limit @/root/deploy.retry

clean:
	docker rm $(shell docker ps -n=1 -q)

$(REBUILD_TAGS):
	#script/assemble_certs
	script/deploy -t $@
