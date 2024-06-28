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
Demonstrate building an ACI Fabric as Code from the ground up using Ansible and AAP.This README includes two demos. 
1. Deploying ACI-as-CODE with csvfiles
2. Brownfield ACI-as-Code with YAML files

## Overview
In both demos we will find a cure for the proverbial ACI GUI `Death by a thousand clicks`!!!

1. Deploying ACI-as-CODE with csvfiles
This demo is for ACI operators who have documented their GUI configurations with spreadsheets/csv files. If the spreadsheet/csv is a source of truth for ACI, then Ansible can easily configure the ACI fabric using the read_csv module + cisco.aci collection 

2. Brownfield ACI-as-Code with YAML files
This demo is for ACI operators who have an existing ACI fabric with many configurations. Using the cisco.aci collection and roles, we can query the existing managed objects and save as YAML configuration files. These variables are subsequently mapped the to the appropriate ansible modules to modify existing or deploy new ACI configurations. 

## Devnet ACI Sandbox
The hosts.yml file in this demo can be modified to run in the Cisco Devnet ACI always on or reserved sandboxes. The latter requires a vpn connection.

### Always On:
apic_host: sandboxapicdc.cisco.com
apic_username: 'admin'
apic_password: '!v3G@!4@Y'
https://sandboxapicdc.cisco.com

# Demo1: Deploying ACI-as-CODE with csvfiles
- Click on and walk through the 0-ACI-as-Code-Workflow to Deploy ACI fabrics as Code
- Watch the output in the ACI-Day0-1-Config-Staging
- Take a look at the ACI-Day2-Health-Check.  Talk about what goes into the health score and why it is important.

# Demo2: Brownfield ACI-as-Code with YAML files
- Click on and walk through the 0-ACI-as-Brownfield-Workflow to injest the current ACI fabric configurstions as 
- Review the defaults variables `(learned configs)` in each brownfield role
- Review the vars variables to add new configurations to the ACI fabric
- In VSCode modify an existing tenant configuration in the defaults vars and save and push to gitea repository with git extension or CLI.
~~~
git add all
git commit -m 'changed exting tenant'
git push
~~~ 
- Return to AAP JOBs to approve change control step in the 0-ACI-as-Brownfield-Workflow
- Review the job output for ACI-Brownfield-Deploy job-template (new configs) and ACI-Brownfield-Config) job-template for (Existing Configs)
- Take a look at the ACI-Day2-Health-Check.  Talk about what goes into the health score and why it is important.

# Key Takeaways
* Easy migration from postman to Ansible with csv files
* No need to work with the APIC GUI or APIs directly
* Easy migration to IaC methodologies (gitops, webhook triggers etc)
* Easily convert existing ACI managed objects to YAML configurations
* Easily creat health checks to verify the operation state of the ACI fabric

## Return to Demo Menu
 - [Menu of Demos](../README.md)


