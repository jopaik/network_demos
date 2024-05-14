[![Lab](https://img.shields.io/badge/Try%20Me-EE0000?style=for-the-badge&logo=redhat&logoColor=white)](https://red.ht/aap-product-demos)
[![Dev Spaces](https://img.shields.io/badge/Customize%20Here-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://workspaces.openshift.com/f?url=https://github.com/ansible/product-demos)

# Ansible Network Demos

This is a centralized location for Ansible Network Demos. This project is a collection of use cases implemented with Ansible for use with the Ansible Automation Platform.

## Menu of Demos
- [Network Backups GIT](network_backups_git/README.md)
   * DEMO NAME: network_backups_git
   * Validated Content: network.backup 
   * Self Service Survey
   * Intended config "configuration drift"
   * Restore Configs
- [Network Compliance Dashboard](network_compliance_dashboard/README.md)
   * DEMO NAME: network_compliance_dashboard
   * Network Facts
   * JINJA2 HTML template
- [Network Compliance Checks Remediations](network_compliance_checks_remediations/README.md)
   * DEMO NAME: network_compliance_checks_remeditions
   * [ Demo Video](https://youtu.be/S1k41RMfieoa?feature=shared)
   * Network Resource Modules
   * Workflows
   * Self Service Survey
   * Check Mode/Run Mode (ntp,snmp,logging,and acls)
   * Handlers
   * Cisco STIG
- [Scoped Configuration Management](scoped_configuration_management/README.md)
   * DEMO NAME: scoped_configuration_management
   * Validated Content: `network.base` 
   * Operations: Persist, Deploy, Detect, Remediate
   * BGP
- [Completed Ansible Network Automation Workshop 101 Demo ](completed_ansible_network_automation_workshop_101_demo/README.md)
   * DEMO NAME: completed_ansible_network_automation_workshop_101_demo
   * Network Backups and Restore to a server
   * Network User
   * Network Banner
   * Workflow
   * Self Service Survey
- [Network Access List](network_access_list/README.md)
   * DEMO NAME: network_access_list
   * Deploy ACLS with Validated Content
   * Detect incorrect ACL Entries
   * Remdiate ACL entries
   * Make changes to existing ACLs and Entries
- [Network SNOW](network_snow/README.md)
   * DEMO NAME: network_snow
   * Compliance Checks 
   * Automatically Open SNOW Inicidents (tickets)
   * Resolve Issues
   * Close Tickets 
   * Dynamic Inventory from CMDB
   * Get Facts
- [Cisco ACI](cisco_aci)
   * DEMO NAME: cisco_aci
   * Deploy ACI fabrics as Code
   * Make Health Checks from Ansible to Validate ACI State
- [Cisco DNAC](cisco_dnac)
   * DEMO NAME: cisco_dnac
   * Dynamic Ansible Inventory
   * Backup DNAC configs to Git Repo
   * Use Ansible collection to make compliance checks against DNAC device configs
- [Cisco ISE](cisco_ise)
   * DEMO NAME: cisco_ise
   * Get Config Info
   * Get Device Info
   * Get Endpoint Info
- [Cisco Meraki](cisco_meraki)
   * DEMO NAME: cisco_meraki
   * WIP
- [NetBox](netbox)
   * DEMO NAME: netbox
   * Asible + Netbox SSOT 
   * Dynamic Inventory
   * Config Drift Checks
- [Network Troubleshooting](network_troubleshooting)
   * wip


# Getting Started

## Using this project

This project is tested for compatibility with the [demo.redhat.com Ansible Network Demos]([red.ht/aap-product-demos](https://demo.redhat.com/catalog?search=network&item=babylon-catalog-prod%2Fansiblebu.aap2-workshop-networking-automation.prod)) lab environment.\

Some of these require "always-on" systems available from Cisco devnet, or from Cisco dCloud.  These dependencies will be documented in the demo README.md file.

> NOTE: demo.redhat.com is available to Red Hat Associates and Partners with a valid account.

The following steps only take a few minutes to prep all the demos.
1. wget https://gitlab.com/redhatautomation/network_demos/-/raw/main/gitea/gitea.yml

2. ansible-navigator run -m stdout gitea.yml
   > For more information on these first two steps, see the full detauls here [gitea/README.md](gitea/README.md)

3. If it is not already created for you, add an Execution Environment called `product-demos`

     - Name: product-demos
     - Image: quay.io/acme_corp/product-demos-ee:latest
     - Pull: Only pull the image if not present before running

4. If it is not already created for you, create a Project called `Network Demos` with this repo as a source. NOTE: if you are using a fork, be sure that you have the correct URL. Update the project.

5. Create a Job Template called `Setup - Network Demos` with the following configuration:

     - Name: Setup - Network Demos
     - Inventory: Workshop Inventory
     - Exec Env: product-demos
     - Organization: Red Hat network organization
     - Playbook: setup_demo.yml
     - Credentials:
        - Type: Red Hat Ansible Automation Platform
        - Name: Controller Credential
     - Extra vars:
         demo: <use `DEMO NAME` from the descriptions above>

6. Run the `Setup - Network Demos` Job template.





[Privacy statement](https://www.redhat.com/en/about/privacy-policy) | [Terms of use](https://www.redhat.com/en/about/terms-use) | [Security disclosure](https://www.ansible.com/security?hsLang=en-us) | [All policies and guidelines](https://www.redhat.com/en/about/all-policies-guidelines)
