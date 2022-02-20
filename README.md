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
you can simply run the command down below, this will prepare all needed files to execute your keeper
```
./make.sh setup
```
# Run
Run the keeper using Docker Compose
```
./make.sh deploy

```
Airflow runs on port 80 so navigate to http://localhost to access the UI. Once things have booted up, log in with username `airflow` and password  `airflow`.

## Run in debug mode
Use:
```
./make.sh check
```
## Optional
* You can change scheduling from GUI
* Navigate to `Admin > Variables` and add the following to change dag schedule:
  * `distribution-schedule-interval` - Dag `distribute` (Default - `0 * * * *`)
  * `harvester-schedule-interval` - Dag `harvester` (Default - `0 * * * *`)
  * `watch-schedule-interval` - Watch stream dag (Default - `50 * * * *`)
  * `tellor-schedule-interval` - Reporting to Tellor (Default - `*/5 * * * *`)
  * `swap-schedule-interval` - Swap RIC stream to matic (Default - `0 * * * *`)
  * `block-poll-schedule-interval` - Block poll (Default - `*/15 * * * *`)
  * `close-schedule-interval` - Close streams (Default - `None`)
  * `max-gas-price` - To set the max gas price (Default - `33`)
