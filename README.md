# JupyterHub deployment for DS8

This repository contains an Ansible playbook for launching JupyterHub for the
Data Science 8 class at Berkeley. It is almost entirely based on the deployment for [Computational Models of Cognition](https://github.com/compmodels/jupyterhub-deploy). That course utilized Rackspace infrastructure and GitHub for authentication while this deployment will use Azure and Google OAuth. There are also some minor changes in the docker and NFS configurations.

For detailed information, please see @jhamrick's README.md in the compmodels repository linked above.
