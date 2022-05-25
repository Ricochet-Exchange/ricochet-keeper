# Ricochet Gelato
This repository contains scripts for adding keeper tasks for Ricochet Exchange to gelato.

## Setup
Create a .env variable file suing .env.example
```
ALCHEMY_ID=
PRIVATE_KEY=
```
## Execute Scripts
- Make sure all the contants for launchpad and market are up to date in `constants`
- Once your have added the env variables, you can run the scripts to add tasks to gelato
```
yarn launchpad --network matic
yarn market --network matic
```

