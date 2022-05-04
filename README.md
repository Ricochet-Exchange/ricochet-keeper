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
keeper_repository = ""                  # repository used for deployement
keeper_repository_branch = ""           # branch to deploy - defaults to master
SWAPPER_ADDRESS_KEY = ""                # SWAPPER_ADDRESS key
CLOSER_ADDRESS_KEY = ""                 # CLOSER_ADDRESS key
DISTRIBUTOR_ADDRESS_KEY = ""            # DISTRIBUTOR_ADDRESS key
DISTRIBUTOR_V2_ADDRESS_KEY = ""         # DISTRIBUTOR_V2_ADDRESS key
REPORTER_ADDRESS_KEY = ""               # HARVESTER_ADDRESS key
REPORTER_ADDRESS_KEY = ""               # REPORTER_ADDRESS key
REX_BANK_KEEPER_ADDRESS_KEY = ""        # REX_BANK_KEEPER_ADDRESS key
SWAPPER_ADDRESS = ""                    # SWAPPER_ADDRESS
CLOSER_ADDRESS = ""                     # CLOSER_ADDRESS
DISTRIBUTOR_ADDRESS = ""                # DISTRIBUTOR_ADDRESS
DISTRIBUTOR_V2_ADDRESS = ""             # DISTRIBUTOR_V2_ADDRESS
HARVESTER_ADDRESS = ""                  # HARVESTER_ADDRESS
REPORTER_ADDRESS = ""                   # REPORTER_ADDRESS
REX_BANK_KEEPER_ADDRESS = ""            # REX_BANK_KEEPER_ADDRESS
gateway_uri = ""                        # infura or quicknode gateway uri
gateway_wss = ""                        # infura or quicknode gateway wss
airflow_password = ""                   # Airflow password
postgres_password = ""                  # Postgresql password
aws_public_key = ""                     # ssh public key to connect to EC2 instance
aws_access_key= ""                      # aws credentials
aws_secret_key= ""                      # aws credentials
aws_region= ""                          # aws region
egress_cidr_blocks = ""                 # egress cidr_block list - defaults to ["0.0.0.0/0"]
ingress_cidr_blocks_ssh = ""            # ssh ingress cidr_block list - defaults to ["0.0.0.0/0"] 
ingress_cidr_blocks_web = ""            # web ingress cidr_block list - defaults to ["0.0.0.0/0"] 
ingress_cidr_blocks_keeper = ""         # keeper ingress cidr_block list - defaults to ["0.0.0.0/0"] 
```

Move to terraform directory and initialize terraform
```
cd terraform && terraform init
```

Deploy keeper using the command down below. 
Once the deployment finished you can connect to the outputted ip address
```
terraform apply
```
