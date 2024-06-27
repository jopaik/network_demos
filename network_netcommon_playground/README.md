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
5. Run the Network-Netcommon-Facts Job template to gather and write the exiting configuration files for single source of truth (SSOT) to the gitea master branch.
6. Use VSCode to review the `host_vars` in the network-demos-repo/network_netcommon_playground
~~~
git pull
~~~
click on facts.yaml for each router to review configs
7. Review the `network_netcommon_facts.yml` playbook
8. Make an OOB change to rtr1  
9. Run the Network-Netcommon-Diff jo-template and locat the OOB change made above
10. Make an addition to the rtr1 tunnel interfaces in host_vars facts.yaml 
* Note not all of the resource modules are enabled in the demo
* Remember to push your change to the gitea repo using VSCode git extension or CLI
~~~
git add all
git commit -m 'rtr1 changed'
git push
~~~
11. Run the Network-Netcommon-Deploy job template to add and `facts.yaml' remove the changes made from the OOB change
12. Validate the changes were made.
13. Run the Network-Netcommon-Ping Job-template

# Key Takeaways
* An alternative to te network.base validated roles when additional customization is desired
* Provides a Multi-vendor automation solution for Ansible
* Additional abstractions to remove vendor nuances and CLI knowledge

## Return to Demo Menu
 - [Menu of Demos](../README.md)


