## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Connect to Netbox Demo server to create and copy an API token
https://netbox-demo.netboxlabs.com/ user=admin pass=admin
2. Launch the Network-Netbox-Setup Job Template to configure a device and settings on Netbox
3. Review the Netbox GUI (devices, templates etc)
4. Add the API Token to Netbox inventory source to sync with Netbox as a dynamic inventory
5. Review the Netbox Inventory on AAP
6. Launch the Network-Netbox-Facts job-template to demonstrate using the Inventory for rtr1
7. Launch the Network-Netbox-Compare-Configs job-template to compare the running config to the netbox rendered config template.
8. Verify Config drift checks by changing the config on rtr1. Also not the serial number, IPs, and cert informaiton will be different in every demo POD.

# Netbox

[Table of Contents](#table-of-contents)
- [Step 1 - Netbox Demo Server](#step-1-netbox-demo-server)
- [Step 2 - Network-Netbox-Setup Workflow Template](#step-2-network-netbox-setup-workflow -template)
- [Step 3 - Review the Netbox GUI](#step-3-review-the-netbox-gui)
- [Step 4 - Add the API Token](#step-4-add-the-api-token)
- [Step 5 - Review the Netbox Inventory on AAP](#step-5-review-the-netbox-inventory-on-aap)
- [Step 6 - Launch the Network-Netbox-Facts job-template](#step-6-launch-the-network-netbox-facts-job-template)
- [Step 7 - Launch the Network-Netbox-Compare-Configs job-template](#step-7-)
- [Step 8 - Verify Config drift checks by changing the config on rtr1](#step-8-)

## Objective
To integrate Ansible with Netbox as a single source of truth (SSOT)

## Overview
The netbox.netbox collection allows Ansible to manage Netbox easily from the API. In this demo we use Ansible to check for config drift from routers config managed via Netbox. 

### Step 1 - Netbox Demo Server
Connect to Netbox Demo server to create and copy an API token
https://netbox-demo.netboxlabs.com/ user=admin pass=admin

### Step 2 - Network-Netbox-Setup Workflow Template
Launch the Network-Netbox-Setup Workflow Template to configure a device and settings on Netbox

### Step 3 - Review the Netbox GUI 
Review the Netbox GUI (devices, templates etc)

### Step 4 - Add the API Token
Add the API Token to Netbox inventory source to sync with Netbox as a dynamic inventory

### Step 5 - Review the Netbox Inventory on AAP

### Step 6 - Launch the Network-Netbox-Facts job-template 
Launch the Network-Netbox-Facts job-template to demonstrate using the Inventory for rtr1

### Step 7 - Launch the Network-Netbox-Compare-Configs job-template 
Launch the Network-Netbox-Compare-Configs job-template to compare the running config to the netbox rendered config template.

* Note, that every router from RHDP will have different IP addresses, certs etc. These nuances will show as Diffs 

### Step 8 - Verify Config drift checks 
Verify Config drift checks by changing the config on rtr1 and relaunching the Network-Netbox-Compare-Configs job-template

* For example, add a new loopback 100 or something simular to simulate an out of band (OOB)change. 


# Key Takeaways
* Configure Netbox with AAP as an alternative to the GUI
* Use Netbox as a dynamic inventory source for Ansible
* Comapare Netbox device configs as a source of truth for config drift.
*
## Return to Demo Menu
 - [Menu of Demos](../README.md)