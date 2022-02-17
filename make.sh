#!/bin/bash

# Airflow variables
export AIRFLOW__CORE__FERNET_KEY=your_super_secret_key

# the directory containing the script file
dir="$(cd "$(dirname "$0")"; pwd)"
cd "$dir"

log()   { echo -e "\e[30;47m ${1^^} \e[0m ${@:2}"; }        # $1 uppercase background white
info()  { echo -e "\e[48;5;28m ${1^^} \e[0m ${@:2}"; }      # $1 uppercase background green
warn()  { echo -e "\e[48;5;202m ${1^^} \e[0m ${@:2}" >&2; } # $1 uppercase background orange
error() { echo -e "\e[48;5;196m ${1^^} \e[0m ${@:2}" >&2; } # $1 uppercase background red

# log $1 in underline then $@ then a newline
under() {
    local arg=$1
    shift
    echo -e "\033[0;4m${arg}\033[0m ${@}"
    echo
}

usage() {
    under usage 'call the Makefile directly: make up
      or invoke this file directly: ./make.sh up'
}


# check if docker-compose is intalled 
check-docker-compose() {
    if [[ -z $(which docker-compose) ]]
    then
        log checking docker-compose
	echo "please install docker-compose"
    else
        log skip docker-compose is installed
    fi
}

# check if  if missing (no update)
check-docker() {
    if [[ -z $(which docker) ]]
    then
        log check docker
	echo "please install docker https://docs.docker.com/engine/install/"
    else
        log skip docker is installed
    fi
}


deploy-keeper() {
    # setup all required environment variables
    yarn audit 
    echo "tests here"

    [[ -f "$dir/.env" ]] && { log skip .env file already exists; return; }
    info create .env file


# if `$1` is a function, execute it. Otherwise, print usage
# compgen -A 'function' list all declared functions
# https://stackoverflow.com/a/2627461
FUNC=$(compgen -A 'function' | grep $1)
[[ -n $FUNC ]] && { info execute $1; eval $1; } || usage;
exit 0
