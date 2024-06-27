## Return to Demo Menu
 - [Menu of Demos](../README.md)

## Netcommon Playground


## Objective
The ansible.netcommon collection provides a layer of abstraction to normalize automation across multi-vendor nework devices.

## Overview
In this demo we will leverage the netcommon collection to complete common network use cases across Cisco, Juniper, and Arista network devices.

## Use Cases Provided
* Backups and Restores
* Staging upgrades or downloading files
* Command Lines and Configs
* Managing Resource Modules and Single Source of Truth (SSOT)
* Pings

# Demo
1. Run the Network-Netcommon-Backups Job Template.
2. Select the three device groups and provide a name for the branch to save your backup files
3. Review the network device backup files and playbooks in gitea user-gitea pass=gitea
3. Make an out-of-band (OOB) change to rtr1 and save
4. Run the Network-Netcommon-Restore job template (`selecting your backup branch`) and validate the router change was removed.
5. In the Admin panel of the APIC GUI show the snapshot of the config that was saved for a rollback
6. Review the health score results or a post change health check



# Key Takeaways
* Easy migration from postman to Ansible with csv files
* No need to work with the APIC GUI or APIs directly
* Easy migration to IaC methodologies (gitops, webhook triggers etc)

## Return to Demo Menu
 - [Menu of Demos](../README.md)


