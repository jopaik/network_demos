
# ACI Network as Code Demo
Fork this repo to provide the necessary files to run this demo.
The Demo is meant to run from the main and staging branches. 

## Install AAP 2.x (Free Trial)
https://www.ansible.com/products/automation-platform

## controller.yml
This playbook can be modified to configure your Ansible Automation Platform Controller "Tower" for the demo

## Devnet ACI Sandbox
The hosts.yml file in this demo can be modified to run in the Cisco Devnet ACI always on or reserved sandboxes. The latter requires a vpn connection.

### Always On:
apic_host: sandboxapicdc.cisco.com
apic_password: '!v3G@!4@Y'
https://sandboxapicdc.cisco.com


### Prepare
Run the prepare_env.yml first to setup the reservered or always on sandbox with pre ports and tenants. 


