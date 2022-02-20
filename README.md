# Ricochet Keeper
This repository contains [Apache Airflow DAGs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html) for executing keeper operations for Ricochet Exchange.

# Before you start your keeper
Edit te .vars file with your adresses and private keys, you can use a BIP39 tool generator to generate some adresses
```
You will need to change all of the variables in the .vars file

```
:information_source: This will take a while the first time you do it
:warning: In order to secure your install you must change those default values !

# Setup
After setting up all the variables in .vars 
you can simply run the command down below, this will prepare all needed files and initialize the database
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
