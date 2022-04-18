### Test your changes 

In order to test your changes you need to have aws subscription, aws-cli and terraform installed.
This mechanism is usefull to test any changes to the keepers configuration, especially changes in DAGS.

Fill  the variables down below in terraform.tfvars by specifing the fork/branch that contains your changes and follow the instructions for terraform deployment in README.md     
keeper_repository = ""                  # repository used for deployement
keeper_repository_branch = ""           # branch to deploy - defaults to master

If you had already deployed a keeper on the same machine, in some cases you could need to start with a clean deployment, the two commands down below will delete any data related to your keeper deployment, be careful
docker system prune -a 
docker volume prune
