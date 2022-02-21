#!/bin/bash

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
check() {
    if [[ -z $(which docker-compose && which docker) ]]
    then
        log checking docker-compose
	echo "please make sure that docker and docker-compose are installed"
    else
        log skip docker-compose and docker are installed
    fi
}

setup() {
    # install keeper with all required variables
    source .vars
    envsubst < variables.tmpl.json > variables.json
    envsubst < connections.tmpl.json > connections.json
    envsubst < secrets.tmpl > secrets.sh
    chmod +x secrets.sh && ./secrets.sh
    mkdir -p ./logs ./plugins
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    docker-compose up airflow-init
}

deploy() {
    # run the keeper via docker-compose
    docker-compose up -d

}    

debug() {
    # this is to see a more verbose output
    docker-compose up

}

clean() {
    # run the keeper via docker-compose
    docker-compose down --volumes --rmi all
    git restore docker-compose.yml
}
# if `$1` is a function, execute it. Otherwise, print usage
# compgen -A 'function' list all declared functions
# https://stackoverflow.com/a/2627461
FUNC=$(compgen -A 'function' | grep $1)
[[ -n $FUNC ]] && { info execute $1; eval $1; } || usage;
exit 0
