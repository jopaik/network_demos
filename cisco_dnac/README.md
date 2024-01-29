## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Cisco DNAC 

## Table of Contents
- [Step 1 - Variables](#step-1-variables)
- [Step 2 - Using the Terminal](#step-2-using-the-terminal)
- [Step 3 - Run Playbook](#step-3-run-playbook)
- [Step 4 - Commit to git](#step4-commit-to-git)

# Summary of steps
1. Review the Current Cisco Devnet Always On DNAC Network Device Inventory 
`https://sandboxdnac.cisco.com user=devnetuser password=Cisco123!`
2. Launch the DNAC-Config-Retrieve job-template and select the devices Sw1-4 that are gleaned from the dnac_dynamic inventory source
3. Review the config backups that are saved to the gitea main branch with timestamps.
`cisco_dnac/backups`
4. Launch the Dnac-Compliance job-template to check if hte current Device Software Versions are in compliance.

## Objective
Demonstrate Ansible working `Better Together` with Cisco DNAC by saving the DNAC device configuration backups to a git repository. The Git repo is foundational for infrastucture as code and offers a method for managing single source of truth and configuration drift "diff" checks. The second part of the demo highlights AAP's ability to glean device information from DNAC to use for easy to impliment compliance checks.
## Overview
In this demo we will check configurations from DNAC `Catalyst Center` as a Single Source of truth for Ansible. In turn we can reconcile any confiuration drift before making changes originated in AAP or DNAC. In the second part of the demo we use DNAC device information for compliance checks or optionally pass DNAC config datato other CMDB systems etc.

## Devnet ACI Sandbox
The hosts.yml file in this demo can be modified to run in the Cisco Devnet always on or reserved sandboxes. The latter requires a vpn connection.

### Always On:
dnac_server: https://sandboxdnac.cisco.com
dnac_username: devnetuser
dnac_password: Cisco123!

## Step 1 - DNAC GUI
1. Review the Current Cisco Devnet Always On DNAC Network Device Inventory 
`https://sandboxdnac.cisco.com user=devnetuser password=Cisco123!`

[DNAC](../images/dnac.png)


## Return to Demo Menu
 - [Menu of Demos](../README.md)

