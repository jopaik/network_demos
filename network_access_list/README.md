# Managing Network ACLS with Resource Modules



## Demo Info

* 1-check_acl.yml: This playbook provides a check to identify the "meetup" ACL is present on both the Cisco and Jumiper routers. It uses Gather and Assertions.
* 2-gather_acls: This playbook gathers the existing ACLs and ACE entries and saves them as a YAML host variable file to run playbooks against
* 3-gather_drift.yml: This playbook creates a diff file to identify deltas between the intended ACL configuration in the host_vars versus the actual running configuration
* 4-merge.yml: This playbook pushes ACL configuration additions to the routers
* 5-replace.yml: This playbook changes existing ACL/ACE entries on the router.
* 6-overwrite.yml: This playbook adds or removes "overwrites" sections of the ACLs
* 7-delete.yml: This plabook removes the entire ACLs
* 8-rendered: This playbook converts the structure data in vars files to the native configs that are sent the router. (ie., CLI or netconf etc.). This is read only.
