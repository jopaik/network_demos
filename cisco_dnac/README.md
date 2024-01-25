## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Launch the Dnac-Device-ID job-template for Ansible to learn the existing device IDs for the DNAC configurations.
2. Launch the Dnac-configs job-template and select a device ID to print and save a devices's configuration 
3. Launch the Dnac-intended config to make there are no diffs between the network device's running config and the dnac source of truth 
(SOT) before push a change to da device from ansible.

## Objective
Demonstrate Ansible working `Better Together` with DNAC by checking the DNAC configurations 
agianst the device's existing configuration to manage config drift.
## Overview
In this demo we will check configurations from DNAC `Catalyst Center` as a Single Source of truth for Ansible. In turn we can reconcile any confiuration drift.

## Devnet ACI Sandbox
The hosts.yml file in this demo can be modified to run in the Cisco Devnet always on or reserved sandboxes. The latter requires a vpn connection.

### Always On:
dnac_server: https://sandboxdnac.cisco.com
dnac_username: devnetuser
dnac_password: Cisco123!

## Return to Demo Menu
 - [Menu of Demos](../README.md)

