# Ricochet Keeper
This repository contains [Apache Airflow DAGs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html) for executing keeper operations for Ricochet Exchange.

# Before you start your keeper
Edit te .vars file with your adresses and private keys, you can use a BIP39 tool generator to generate some adresses
```
You will need to change all of the variables in the .vars file
cp .vars.tmpl .vars

```
:information_source: This will take a while the first time you do it
:warning: In order to secure your install you must change those default values 

# Setup
After setting up all the variables in .vars 
run the command down below, this will prepare all needed files and initialize the database
```
./make.sh setup
```
# Execute keeper
Now simply run the keeper using docker compose
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

# Deploy with terraform
Rename terraform template file to terraform.tfvars
```
cp terraform/terraform.{tmpl.tfvars,tfvars}
```

Fill variables contained in that file
```
keeper_repository = ""        # repository used for deployement
keeper_repository_branch = "" # branch to deploy - defaults to master
key1 = ""                     # wallet1 seed
key2 = ""                     # wallet2 seed
key3 = ""                     # wallet3 seed
key4 = ""                     # wallet4 seed
key5 = ""                     # wallet5 seed
key6 = ""                     # wallet6 seed
key7 = ""                     # wallet7 seed
address1 = ""                 # wallet1 address
address2 = ""                 # wallet2 address
address3 = ""                 # wallet3 address
address4 = ""                 # wallet4 address
address5 = ""                 # wallet5 address
address6 = ""                 # wallet6 address
address7 = ""                 # wallet7 address
gateway_uri = ""              # Ethereum gateway config
gateway_wss = ""              # Ethereum gateway config
airflow_password = ""         # Airflow password
postgres_password = ""        # Postgresql password
aws_public_key = ""           # public key used to connect to EC2 instance
aws_access_key= ""            # aws credentials
aws_secret_key= ""            # aws credentials
aws_region= ""                # aws region
```

Move to terraform directory
```
cd terraform
```

Initialize terraform
```
terraform init
```

Deploy keeper
```
terraform apply
```
