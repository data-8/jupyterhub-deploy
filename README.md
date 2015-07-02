# JupyterHub deployment for DS10 / Stat 94

This repository contains an Ansible playbook for launching JupyterHub for the
Data Science 10 / Statistics 94 class at Berkeley. It is almost entirely based on the deployment for [Computational Models of Cognition](https://github.com/compmodels/jupyterhub-deploy). That course utilized Rackspace infrastructure and GitHub for authentication while this deployment will use AWS and Google OAuth. There are also some minor changes in the docker and NFS configurations.

For detailed information, please see @jhamrick's README.md in the compmodels repository linked above.
