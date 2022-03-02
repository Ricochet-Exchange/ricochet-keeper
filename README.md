# Ricochet Keeper
This repository contains [Apache Airflow DAGs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html) for executing keeper operations for Ricochet Exchange.

# Prepare your keeper install
Generate the .vars using the command down below and customize it with your adresses and private keys.
You can use a BIP39 tool generator to generate some adresses.
Adjust schedule variables according to other keepers values.
```
./make.sh init

```
:information_source: This will take a while the first time you do it
:warning: To secure your install you must use different values for each variable in .vars (fernet key is automatically generated) 

# Setup
After setting up all the variables in .vars 
executing the command down below will prepare all needed files and initialize the database
```
./make.sh setup

```
# Execute keeper
once setup step is finished run the keeper using docker compose
```
./make.sh deploy

```
Airflow runs on port 80 so navigate to http://localhost to access the UI. Once things have booted up, log in with username `airflow` and password  `your-airflow-password`.

## Run in debug mode, usefull if the previous command exit with an error
Use:
```
./make.sh check
```
# Clean up you keeper install
run the keeper using docker compose
:warning: this will stop your keeper and delete everything

```
./make.sh clean

```

## Optional
* If needed you can change variables or connections values from GUI
* Navigate to `Admin > Variables`  or `ADMIN > Connctions ` and change your values

# If you have a aws account, you can deploy your keeper using terraform (this is the recomended way, all firewall rules are already set up)

Rename terraform template file to terraform.tfvars
```
cp terraform/terraform.{tmpl.tfvars,tfvars}
```

Fill  all variables contained in terraform.tfvars
you can customize schedule values by editing .vars.tmpl file 
```
keeper_repository = ""        # repository used for deployement
keeper_repository_branch = "" # branch to deploy - defaults to master
key1 = ""                     # address1 key
key2 = ""                     # address2 key
key3 = ""                     # address3 key
key4 = ""                     # address4 key
key5 = ""                     # address5 key
key6 = ""                     # address6 key
key7 = ""                     # address7 key
address1 = ""                 # address1
address2 = ""                 # address2
address3 = ""                 # address3
address4 = ""                 # address4
address5 = ""                 # address5
address6 = ""                 # address6
address7 = ""                 # address7
gateway_uri = ""              # infura or quicknode gateway uri
gateway_wss = ""              # infura or quicknode gateway wss
airflow_password = ""         # Airflow password
postgres_password = ""        # Postgresql password
aws_public_key = ""           # ssh public key to connect to EC2 instance
aws_access_key= ""            # aws credentials
aws_secret_key= ""            # aws credentials
aws_region= ""                # aws region
```

Move to terraform directory and initialize terraform
```
cd terraform && terraform init
```

Deploy keeper using terraform. 
Once the deployment finished you can connect to the outputted ip address
```
terraform apply
```
