## Summary of steps
The following steps only take a few minutes to prep all the demos.
1. wget https://gitlab.com/redhatautomation/network_demos/-/raw/main/gitea/gitea.yml
2. ansible-navigator run -m stdout gitea.yml
3. setup VSCode for git
4. Add your student pod password and run the following command from `network-demos-repo/`
~~~
 ansible-navigator run controller_as_code/setup.yml --eei registry.gitlab.com/redhatautomation/validated-network-ee:latest -m stdout -e "username=gitea git_password=gitea password=<replace-with-lab-student-password>"
~~~