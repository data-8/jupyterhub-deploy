DEPLOY_C="ds/deploy:1"

rootsshkey:
	for h in proxy_server jupyterhub_host jupyterhub_node1 jupyterhub_node2 ; do \
		echo $$h ; \
		ssh ubuntu@$$h 'sudo cp -p /root/.ssh/authorized_keys{,-}; sudo install -o root -m 0600 /home/ubuntu/.ssh/authorized_keys /root/.ssh/authorized_keys' ; \
	done

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
