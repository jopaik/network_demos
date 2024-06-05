
## Return to Demo Menu
 - [Menu of Demos](../README.md)

## Brownfield Resource Modules
This Demo requires acces to the NXOS always on router in Cisco Devnet

Host	              	
sbx-nxos-mgmt.cisco.com	
Username: admin
Password: Admin_1234!
Port: 22
NetConf: 830
NXAPI: 443

## Steps

1. Run the Job-template `network_brownfield_resource_modules` for the brownfield.yml

2. Inspect your host_vars

3. Make a change to the l2 interfaces 

4. Push Change to gitea repo

5. Run the Job-template `network_brownfield_diff` Job template for the diff.yml playbook to identify the difference between the SSOT `host_vars` versus the running configuration on the swith. 

6. Run the `network_brownfield_deploy` Job-template for the deploy.yml playbook 


## Return to Demo Menu
 - [Menu of Demos](../README.md)


 
 