## Return to Part 2 Exercises
* [Part 2 ](../../README.md)


# Exercise 4 - Scoped Configuration Management

[Table of Contents](#table-of-contents)
- [Step 1 - Persist](#step-1-persist)
- [Step 2 - Deploy](#step-2-deploy)
- [Step 3 - Detect](#step-3-detect)
- [Step 4 - Remediate](#step-4-remediate)

## Solution
If needed.
[solution](solution/)

## Objective

Create `job-templates` that use playbooks developed with `validated content` for networks. The main use case is to establish a single `source of truth` for your network environment. The validated content will allow you to gather facts from brownfield devices to simplify creating a single source of truth mapped to the `inventory host_vars`. With a SSOT in mind, we can easily manage `configuration drift` and accept or remediate changes using validated content for networks.

## Overview

The Ansible validated content for networks `network.base` focuses on abstract platform-agnostic network automation and enhances the experience of resource module consumption by providing production-ready content. This network base content acts as the core to the other network validated content, such as `network.ospf` and `network.interfaces`.   

### Step 1 - Persist
The resource_manager role uses the `persist action` to get the facts for a given resource and store it as inventory host_vars. 

1. Create a job-template named `Network-Validated-Persist` with the following parameters.  The machine credential "Workshop Credential" and the Gitlea Student credential type with the "Gitlea Credential".

#### Paremeters:
- name: **Network-Validated-Persist**
- organization: **Red Hat network organization**
- inventory: **Workshop Inventory**
- project: **Student Project**
- playbook: **part2/2-systematic/4-scoped-config-management/persist.yml**
- credentials:
  - "Workshop Credential"
  - "Gitea Credential"
- execution_environment: **"Validated Network"**

2. Review the `persist.yml` playbook located `~/student-repo/part2/2-systematic/4-scoped-config-management/persist.yml`
- Notice how the gitea variables are defined in `vars/git.yml` and the Gitea Credential is used to securely store the password/token. Secondly the resource modules are listed in the `vars/resource` for the play. In turn, the resource_manager role will render a hostvars/.yml file or each resource entry. For this exercise in particular, we are using shell commands to commit and pull directly to the main branch of the gitea project "student-repo". 

- Notice that this playbook includes the role resource_manager. There is no local roles folder in this exercise. The network.base collection is installed in our execution environement container. How does ansible locate this resource_manager role that is included in a collection?
```
ansible.builtin.include_role:
        name: resource_manager
```
In the root of the ansible-network-automation-workshop-201 project directory there is an ansibl.cfg file. In this file we created a roles_path to the network.base validated collection from the EE.
```
roles_path = /usr/share/ansible/collections/ansible_collections/network/base/roles/
```
**Optional task:  List the installed Collections from an AAP Execution Environment**
- `skip to step 3 below if not interested` 

In the AAP Controller adhoc commands can be ran from an inventory group. In the below example we will limit the command to rtr1 from the group since we are actually running the command from the shell on the execution environment container, not the router, when `running` an adhoc command.

- Navigate to inventory/groups to run adhoc commands form the AAP controller. Notice the run command button below.
 ![adhoc](../../images/adhoc1.png)
 - Use the shell command module to run commands similar to the CLI
 - ansible-galaxy collection list will display the installed collections for an EE
 - Limit to a single device in the inventory to save time
 ![adhoc](../../images/adhoc2.png)
 - Select an execution environment. This EE includes the network.base collection
 ![adhoc](../../images/adhoc3.png)
- Select a credential
 ![adhoc](../../images/adhoc4.png)
- Run the adhoc command and locate the network.base in the output.
 ![adhoc](../../images/adhoc5.png)


`Sorry for the tangent...` Lets get back to our `Network-Validated-Persist` job template

3. Launch the `Network-Validated-Persist` job template and review the output.

4. Verify the host_vars entries for each of the four routers in the `part2/2-systematic/4-scoped-config-mangement/host_vars/` of your student-repo project.

5. From the VSCode terminal:
~~~
git pull
~~~
6. Verify from VSCode
~~~
[student@ansible-1 student-repo]$ ls  part2/2-systematic/4-scoped-config-management/host_vars/
rtr1  rtr2  rtr3  rtr4
~~~

7. If you check from the gitea gui it will look something like the following:
- part2/2-systematic/4-scoped-config-mangement/host_vars/
 ![hostvars](../../images/hostvars_persist.png)  


### Step 2 - Deploy
The resource_manager role uses the Deploy action to apply changes to the listed resources. The deploy action works well for additions to the device's configuration because it uses the state of merged. The state of merged will not overwrite any existing configurations.

1. Add a new BGP network prefix "192.168.4.4/32 entry to the "~/student-repo/part2/2-systematic/4-scoped-config-mangement/hostvars/rtr2/bgp_address_family.yaml" configuration file. This entry will advertise the Loopback0 from rtr4.

- Example
~~~
bgp_address_family:
    address_family:
    -   afi: ipv4
        neighbor:
        -   activate: true
            peer: 10.200.200.1
        network:
        -   address: 10.101.101.0/24
        -   address: 10.200.200.0/24
        -   address: 172.18.0.0/16
        -   address: 192.168.2.2/32
        -   address: 192.168.4.4/32
    as_number: '65001'
~~~

2. Complete the git steps for your change. You must save, commit the file in the VSCode IDE and "sync" push to gitea after fixing the file.
![Save](../../images/save_commit.png)

or update from the terminal
~~~
git add --all
git commit -m "deploy"
git push
~~~

3. Create a new playbook `deploy.yml` in `~/student-repo/part2/2-systematic/4-scoped-config-management/` 
- Note the simularity to the persist.yml but this time the action is "deploy". Hint, save time in this playbook by listing only the bgp_address_family resource instead of all the resource modules. Your `deploy.yml` should look like the following.

~~~
---
- name: Deploy configuration files from the resource modules 
  hosts: network,localhost
  gather_facts: false
  vars_files:
    - vars/git.yml
  tasks:
    - name: Clone a Repo to EE 
      ansible.builtin.shell:
        cmd: "{{ git_clone }}"
        chdir: /tmp/
      when: inventory_hostname == 'localhost'
    - name: Network Resource Manager
      ansible.builtin.include_role:
        name: resource_manager
      vars:
        action: deploy
        resources:
          - 'bgp_address_family'
        data_store:
         local: "/tmp/student-repo/part2/2-systematic/4-scoped-config-management/solution/"
      when: inventory_hostname != 'localhost'

    - name: Prepare GIT on EE for Credentials(vars/vault.yml)
      ansible.builtin.shell:
          cmd: "{{ item }}"
          chdir: /tmp/student-repo/
      when: inventory_hostname == 'localhost'
      loop:
          - "{{ git_username }}"
          - "{{ git_email }}"
          - "{{ git_add }}"
          - "{{ git_commit }}"

    - name: Push and Hide Token
      ansible.builtin.shell:
          cmd: "{{ git_push }}"
          chdir: /tmp/student-repo/
      when: inventory_hostname == 'localhost'
      no_log: true
~~~

4. Create the Network-Validate-Deploy job-template with the following parameters.
Hint, you can copy the Network-Validated-Persist job-template and slighlty modify.

* Caution, Whenever you create a net-new playbook, you must sync the "Student Project"in the AAP Controller to have access to the new playbook from a job-template.

![project](../../images/project_sync.png)  

Parameters:
- name: **Network-Validated-Deploy**
- organization: **Red Hat network organization**
- inventory: **Workshop Inventory**
- project: **Student Project**
- playbook: **part2/2-systematic/4-scoped-config-management/deploy.yml**
- credentials: **Workshop Credential**
- execution_environment: **Validated Network**

5. Launch the Network-Validated-Deploy job-template. After the deploy.yml completes, ensure that the playbook "changed" adds the network prefix "192.168.4.4 to rtr2 

- From the stdout filter input "changed" and locate rtr2
![stdout](../../images/stdout.png) 

- Click on changed to take a look at the json output. Locate the 192.168.4.4/32 in the `after` output from the module.
![after](../../images/after.png) 
       
### Step 3 - Detect
The resource_manager role uses the detect action to detect configuration drift in the configured resources of the network devices.

1. Access rtr1 from the VSCode terminal and ssh

~~~
ssh rtr1
~~~

2. Use the CLI to add a network prefix to rtr1 for rtr3's loobback0 that is a mistake. Sometimes OOB changes made from the CLI are prown to mistakes. Ooops you just fat fingered it....

~~~
config t
router bgp 65000
address-family ipv4 
network 192.168.1.3 
end
~~~
3. Create a new playbook named detect.yml. 
Feel free to copy deploy.yml. Simply keep the resource bgp_address_family and change the action to detect. If needed, review the solution folder.

* Caution, you must sync the `Student Project` to have access to the new playbook `deploy.yml`!

4. Create a job-template named `Network-Validatd-Detect` with the following parameters. 
- Feel free to copy a previous jobtemplate to save time.
* Paremeters:
- name: **Network-Validated-Detect**
- organization: **Red Hat network organization**
- inventory: **Workshop Inventory**
- project: **Student Project**
- playbook: **part2/2-systematic/4-scoped-config-management/detect.yml**
- credentials:
  - **Workshop Credential**
- execution_environment: **Validated Network**

5. Launch the `Network-Validated-Detect` and note the configuraiton drift for rtr1.

The rtr1's running config is the before diff in red. The 192.168.1.3 entry is drift from our host_vars (SSOT) becuase it was configured OOB and isn't present in the host_vars.

![drift](../../images/drift.png) 

### Step 4 - Remediate
The resource_manager role uses the remediation action to overrite (add or remove) configuration that are not reconsiled with the host_vars yaml files. In this exercise the host_vars files are our single source of truth (SSOT).

1. edit and save the student-repo/host_vars/rtr1/bgp_address_family.yaml 
Add an entry for rtr3's loopback0 ip address "192.168.3.3"

~~~
bgp_address_family:
    address_family:
    -   afi: ipv4
        neighbors:
        -   activate: true
            neighbor_address: 10.200.200.2
        networks:
        -   address: 10.100.100.0
            mask: 255.255.255.0
        -   address: 10.200.200.0
            mask: 255.255.255.0
        -   address: 172.16.0.0
        -   address: 192.168.1.1
            mask: 255.255.255.255
        -   address: 192.168.1.1
            mask: 255.255.255.255
        -   address: 192.168.3.3
            mask: 255.255.255.255   
        redistribute:
        -   ospf:
                process_id: 1
    as_number: '65000'
~~~

2. Complete the git steps for your change. You must save, commit the file in the VSCode IDE and "sync" push to gitea after making the change to the hostvar file above.
![Save](../../images/save_commit.png)

or update from the terminal
~~~
git add --all
git commit -m "remediate"
git push
~~~

3. Create a new playbook `remediate.yml` in `~/student/part2/2-systematic/4-scoped-config-management/` 
- Note you can use `detect.yml` as a reference but this time the action is "remediate". Hint, save time by listing only the bgp_address_family resource. If needed, you can take a peak in the solutions folder.

4. Create the `Network-Validate-Remediate` job-template with the following parameters.
Hint, you can copy the Network-Validated-Detect job-template and slighlty modify.

* Caution, you must sync the `Student Project` to have access to the new playbook `remediate.yml`!

Parameters:
- name: **Network-Validated-Remediate**
- organization: **Red Hat network organization**
- inventory: **Workshop Inventory**
- project: **Student Project**
- playbook: **part2/2-systematic/4-scoped-config-management/remediate.yml**
- credentials: **Workshop Credential**
- execution_environment: **Validated Network**

5. Launch the `Network-Validated-Remediate` job-template
Ensure that the playbook removes the "errored" 192.168.1.3 network prefix mistake to rtr1 and "changes" adds the network prefix "192.168.3.3 to rtr1. 

### If needed a setup.yml with associated playbooks and hostvars are already available in  ~/student-repo/part2/2-systematic/4-scoped-config-management/solution
       
Congratulations the Validated network.base collection has sucessfully reconciled your routers with the `host_vars` source of truth!  

[Click Here to return to the Ansible Network Automation Workshop](../README.md)


