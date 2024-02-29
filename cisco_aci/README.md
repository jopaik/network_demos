## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Access the ACI Devnet `Always On` sandbox ```https://sandboxapicdc.cisco.com/``` user=admin pass=`!v3G@!4@Y`
2. Review the before fabric access policies (interface and switch policies) and tenants
3. Make sure everyone is aware of the variables that are provided in csv files.
3. Launch the `0-ACI-as-Code-Workflow` workflow-template and complete the survey inputs
4. Review the after fabric access policies (interface and switch policies) and tenants in the APIC GUI
5. In the Admin panel of the APIC GUI show the snapshot of the config that was saved for a rollback
6. Review the health score results or a post change health check


## Objective
Demonstrate building an ACI Fabric as Code from the ground up using Ansible and AAP.

## Overview
In this demo we will find a cure for the proverbial ACI GUI `Death by a thousand clicks`!!!

## Devnet ACI Sandbox
The hosts.yml file in this demo can be modified to run in the Cisco Devnet ACI always on or reserved sandboxes. The latter requires a vpn connection.

### Always On:
apic_host: sandboxapicdc.cisco.com
apic_password: '!v3G@!4@Y'
https://sandboxapicdc.cisco.com

# Key Takeaways
* Easy migration from postman to Ansible with csv files
* No need to work with the APIC GUI or APIs directly
* Easy migration to IaC methodologies (gitops, webhook triggers etc)

## Return to Demo Menu
 - [Menu of Demos](../README.md)


