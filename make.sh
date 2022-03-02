#!/bin/bash
set -ex
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
    under usage ' invoke this file directly: ./make.sh setup'
}


# check if docker-compose is intalled 
init() {
    cp templates/vars.tmpl .vars
    if [[ -z $(which docker-compose && which docker) ]] && [[ ${docker-compose -v} != *2.2.3* ]]
    then
        log check docker and docker-compose
	echo "please make sure that docker and docker-compose version 2.2.3 are installed"
    else
        log skip docker-compose and docker are installed
    fi
}

setup() {
    # install keeper with all required variables
    source .vars
    mkdir variables
    envsubst < templates/variables.tmpl.json > variables/variables.json
    envsubst < templates/connections.tmpl.json > variables/connections.json
    envsubst < templates/secrets.tmpl.sh > secrets.sh
    cp templates/docker-compose.tmpl.yml docker-compose.yml
    chmod +x secrets.sh && ./secrets.sh
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    docker-compose -f docker-compose.yml up airflow-init
}

deploy() {
    # run the keeper via docker-compose
    docker-compose -f docker-compose.yml  up -d && \
    docker exec `docker ps |grep "ricochet-keeper_airflow-webserver" | awk '{ print $1}' ` airflow connections import /opt/variables/connections.json && \
    docker exec `docker ps |grep "ricochet-keeper_airflow-webserver" | awk '{ print $1}' ` airflow variables import /opt/variables/variables.json 
}    

debug() {
    # this is to see a more verbose output
    docker-compose -f docker-compose.yml up

}

clean() {
    # run the keeper via docker-compose
    docker-compose -f docker-compose.yml down --volumes --rmi all
    rm docker-compose.yml
    rm secrets.sh
}
# if `$1` is a function, execute it. Otherwise, print usage
# compgen -A 'function' list all declared functions
# https://stackoverflow.com/a/2627461
FUNC=$(compgen -A 'function' | grep $1)
[[ -n $FUNC ]] && { info execute $1; eval $1; } || usage;
exit 0
