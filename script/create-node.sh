#!/bin/bash

# Before running this script, run sudo azure login.

# We must run as the user with the azure cli
if [ -z "${SUDO_USER}" ]; then
	exec sudo $0 "$@"
fi

if [ -z "$1" ]; then
	echo Usage: $0 VM_NAME
	exit 1
fi

VM_NAME="$1"

azure vm create \
        -v \
        --json \
        --admin-username              ubuntu \
        --name                        ${VM_NAME} \
        --resource-group              data8-0 \
        --storage-account-name        data8sa0 \
        --ssh-publickey-file          ~ubuntu/.ssh/ryan_rsa.pub \
        --vm-size                     Basic_A4 \
        --subnet-id                   data8vn0sn \
        --availset-name               data8as0nodes \
        --nic-name                    nic-${VM_NAME} \
        --vnet-name                   data8vn0 \
        --vnet-subnet-name            data8vn0sn \
        --location                    "West US" \
        --os-type                     Linux \
        --image-urn        canonical:ubuntuserver:14.04.2-LTS:latest && \
azure network nic set --network-security-group-name data8nsg0 \
        data8-0 nic-${VM_NAME}
