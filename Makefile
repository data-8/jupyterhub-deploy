DEPLOY_C="ds/deploy:1"

build:
	docker build -t $(DEPLOY_C) .

run:
	docker run -it \
		-v $$SSH_AUTH_SOCK:/root/agent.sock --env SSH_AUTH_SOCK=/root/agent.sock \
		-v $(shell pwd)/../proxy-certs/:/root/jupyterhub-deploy/proxy-certs \
		-v $(shell pwd)/../certificates/:/root/jupyterhub-deploy/certificates \
		$(DEPLOY_C) /bin/bash

deploy:
	ansible-vault encrypt --vault-password-file vault-password secrets.vault.yml
	ansible-vault encrypt --vault-password-file vault-password users.vault.yml  
	script/assemble_certs
	script/deploy

retry:
	script/deploy --limit @/root/deploy.retry

clean:
	docker rm $(shell docker ps -n=1 -q)
