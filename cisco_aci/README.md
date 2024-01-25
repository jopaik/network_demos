## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Access ACI Devnet `Always On` sandbox ```https://sandboxapicdc.cisco.com/``` user=admin pass=`!v3G@!4@Y`
2. Review the before fabric access policies (interface and switch policies) and tenants
3. Make sure everyone is aware the variables are provided in csv files.
3. Launch the `0-ACI-as-Code-Workflow` workflow-template and complete survey
4. Review the after fabric access policies (interface and switch policies) and tenants
5. In the Admin panel of the APIC GUI show the snapshot of the config that was saved for a rollback


## Objective
Demonstrate building an ACI Fabric as Code from the ground up using Ansible and AAP.

## Overview
In this demo we will find a cure for the ACI GUI `Death by a thousand clicks`!!!

## Devnet ACI Sandbox
The hosts.yml file in this demo can be modified to run in the Cisco Devnet ACI always on or reserved sandboxes. The latter requires a vpn connection.

### Always On:
apic_host: sandboxapicdc.cisco.com
apic_password: '!v3G@!4@Y'
https://sandboxapicdc.cisco.com

## Return to Demo Menu
 - [Menu of Demos](../README.md)


