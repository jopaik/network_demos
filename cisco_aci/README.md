## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Access the ACI Devnet `Always On` sandbox ```https://sandboxapicdc.cisco.com/``` user=admin pass=`!v3G@!4@Y`
2. Review the before fabric access policies (interface and switch policies) and tenants
3. Make sure everyone is aware of the variables that are provided in csv files. (demo1)For demo2 (ACI Brownfield to YAML) please see steps below.
4. Launch the `0-ACI-as-Code-Workflow` workflow-template and complete the survey inputs
5. Review the after fabric access policies (interface and switch policies) and tenants in the APIC GUI
6. In the Admin panel of the APIC GUI show the snapshot of the config that was saved for a rollback
7. Review the health score results or a post change health check


## Objective
Demonstrate building an ACI Fabric as Code from the ground up using Ansible and AAP.This README includes two demos. 
1. Deploying ACI-as-CODE with csvfiles
2. Brownfield ACI-as-Code with YAML files

## Overview
In both demos we will find a cure for the proverbial ACI GUI `Death by a thousand clicks`!!!

1. Deploying ACI-as-CODE with csvfiles
This demo is for ACI operators who have documented their GUI configurations with spreadsheets/csv files. If the spreadsheet/csv is a source of truth for ACI, then Ansible can easily configure the ACI fabric using the read_csv module + cisco.aci collection 

2. Brownfield ACI-as-Code with YAML files
This demo is for ACI operators who have an existing ACI fabric with many configurations. Using the cisco.aci collection and roles, we can query the existing managed objects and save as YAML configuration files. These variables are subsequently mapped the to the appropriate ansible modules to modify existing or deploy new ACI configurations. Optional, check for configuration drift.

## Devnet ACI Sandbox
The hosts.yml file in this demo can be modified to run in the Cisco Devnet ACI always on or reserved sandboxes. The latter requires a vpn connection.

### Always On:
apic_host: sandboxapicdc.cisco.com
apic_username: 'admin'
apic_password: '!v3G@!4@Y'
https://sandboxapicdc.cisco.com

# Demo1: Deploying ACI-as-CODE with csvfiles
1.  Click on and walk through the 0-ACI-as-Code-Workflow to Deploy ACI fabrics as Code
2.  Watch the output in the ACI-Day0-1-Config-Staging
3.  Take a look at the ACI-Day2-Health-Check.  Talk about what goes into the health score and why it is important.

# Demo2: Brownfield ACI-as-Code with YAML files
1. Launch the 0-ACI-as-Brownfield-Workflow to injest the current ACI fabric configurstions as code.
2.  Review the defaults variables `(learned configs)` in each brownfield role
3.  Review the vars variables that are pre-loaded to provide an example of adding a new configuration to the ACI fabric
4. In VSCode modify an existing tenant configuration in the brownfield_tenant_deploy/defaults/tenants.yml vars. Adding descriptions to existing tenants is a recommended here.

#### Save and Push changes from vscode to gitea
~~~
git add all
git commit -m 'changed exting tenant'
git push
~~~ 
5.  Return to AAP JOBs to approve change control step in the 0-ACI-as-Brownfield-Workflow
6.  Review the job output for ACI-Brownfield-Deploy job-template (new configs) and ACI-Brownfield-Config job-template for (Existing Configs)
7.  Take a look at the ACI-Day2-Health-Check.  Talk about what goes into the health score and why it is important.
8. Config Drift with Diff

#### step 1 - Rerun the 0-ACI-as-Brownfield-Workflow 
This time we will pull in the changes made in the afore mentioned `vars` becuase they become existing configurations in the default folders written by the playbooks in each role.

It's ok to stay `paused` at the approval stage of the workflow for this exercise.

#### sync your local repo
~~~
git pull
~~~

#### step 2 - Change directories to the `brownfield_tenant_deploy/defaults/main
Now you will be able to locate the tenants.yml diff the previous defaults/main/tenants.yml in the repo.

#### step 3 - Locate the files from the commit comnents
 Locate the comments that state: "Updates made by ansible with play: ACI Brownfield to YAML Collection"
The way to see the comments is:
~~~
git log --pretty=full
~~~
#### step 4 - Run the git Diff from VSCode terminal
~~~
$ git diff 70bf1cd109cb8effe60d1b7b2741cbc0af87f7cd  1468ceb725eabbe60f3207aa107ba27e7b433ec2 defaults/main/tenants.yml 
diff --git a/cisco_aci/roles/brownfield_tenant_deploy/defaults/main/tenants.yml b/cisco_aci/roles/brownfield_tenant_deploy/defaults/main/tenants.yml
index ace4a08..861a07e 100644
--- a/cisco_aci/roles/brownfield_tenant_deploy/defaults/main/tenants.yml
+++ b/cisco_aci/roles/brownfield_tenant_deploy/defaults/main/tenants.yml
@@ -2,13 +2,13 @@ changed: false
 tenants:
 -   fvTenant:
         attributes:
-            annotation: orchestrator:ansible
+            annotation: ''
             childAction: ''
             descr: ''
             dn: uni/tn-infra
             extMngdBy: ''
             lcOwn: local
-            modTs: '2024-07-26T21:29:16.090+00:00'
+            modTs: '2024-07-26T18:45:33.331+00:00'
             monPolDn: uni/tn-common/monepg-default
             name: infra
             nameAlias: ''
@@ -19,13 +19,13 @@ tenants:
             userdom: all
 -   fvTenant:
         attributes:
-            annotation: orchestrator:ansible
+            annotation: ''
             childAction: ''
             descr: ''
             dn: uni/tn-mgmt
             extMngdBy: ''
             lcOwn: local
-            modTs: '2024-07-26T21:29:17.620+00:00'
+            modTs: '2024-07-26T18:45:32.766+00:00'
             monPolDn: uni/tn-common/monepg-default
             name: mgmt
             nameAlias: ''
@@ -36,13 +36,13 @@ tenants:
             userdom: all
 -   fvTenant:
         attributes:
-            annotation: orchestrator:ansible
+            annotation: ''
             childAction: ''
             descr: ''
             dn: uni/tn-common
             extMngdBy: ''
             lcOwn: local
-            modTs: '2024-07-26T21:29:19.190+00:00'
+            modTs: '2024-07-26T18:45:30.682+00:00'
             monPolDn: uni/tn-common/monepg-default
             name: common
             nameAlias: ''
@@ -53,13 +53,13 @@ tenants:
             userdom: all
 -   fvTenant:
         attributes:
-            annotation: orchestrator:ansible
+            annotation: ''
             childAction: ''
-            descr: Aug 6 demo
+            descr: ''
             dn: uni/tn-Heroes
             extMngdBy: ''
             lcOwn: local
-            modTs: '2024-07-26T21:29:20.679+00:00'
+            modTs: '2024-07-26T18:48:12.549+00:00'
             monPolDn: uni/tn-common/monepg-default
             name: Heroes
             nameAlias: ''
@@ -70,13 +70,13 @@ tenants:
             userdom: ':all:'
 -   fvTenant:
         attributes:
-            annotation: orchestrator:ansible
+            annotation: ''
             childAction: ''
-            descr: Aug 6 modified by Ansible
+            descr: ''
             dn: uni/tn-SnV
             extMngdBy: ''
             lcOwn: local
-            modTs: '2024-07-26T21:29:22.188+00:00'
+            modTs: '2024-07-26T18:48:23.552+00:00'
             monPolDn: uni/tn-common/monepg-default
             name: SnV
             nameAlias: ''
@@ -85,21 +85,4 @@ tenants:
             status: ''
             uid: '15374'
             userdom: ':all:'
--   fvTenant:
-        attributes:
-            annotation: orchestrator:ansible
-            childAction: ''
-            descr: Created with AAP2.4
-            dn: uni/tn-Ansible
-            extMngdBy: ''
-            lcOwn: local
-            modTs: '2024-07-26T21:26:29.391+00:00'
-            monPolDn: uni/tn-common/monepg-default
-            name: Ansible
-            nameAlias: ''
-            ownerKey: ''
-            ownerTag: ''
-            status: ''
-            uid: '15374'
-            userdom: ':all:'
 failed: false
~~~

# Key Takeaways
* Easy migration from postman to Ansible with csv files
* No need to work with the APIC GUI or APIs directly
* Easy migration to IaC methodologies (gitops, webhook triggers etc)
* Easily convert existing ACI managed objects to YAML configurations
* Easily create health checks to verify the operation state of the ACI fabric
* Infra as Code anf GitOps allow for easy diff checks to manage configuration drift etc

## Return to Demo Menu
 - [Menu of Demos](../README.md)


