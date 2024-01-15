### The setup.yml playbook will configure the all of the necessary controller constructs up to 3-dynamic-documentation

Run the `ansible-navigator` command with the `run` argument and -m stdout as well as `extra-vars` -e

```bash
$ ansible-navigator run setup.yml -m stdout -e "username=gitea git_password=gitea password=<insert-lab-password>"