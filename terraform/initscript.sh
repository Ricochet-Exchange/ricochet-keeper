#!/bin/bash
set -e
DIRECTORY=/home/ubuntu/ricochet-keeper
DOCKER_CONFIG=/home/ubuntu/.docker

echo "Prepare install"
apt-get install -y ca-certificates curl gnupg lsb-release sudo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io
usermod -a -G docker ubuntu
sudo -u ubuntu mkdir -p $DOCKER_CONFIG/cli-plugins
sudo -u ubuntu curl -SL https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x /home/ubuntu/.docker/cli-plugins/docker-compose
ln -s /home/ubuntu/.docker/cli-plugins/docker-compose /usr/bin/docker-compose

echo "Fail2ban deployment"
apt-get install -y fail2ban
rm /etc/fail2ban/jail.d/defaults-debian.conf
echo -e "[sshd]\nenabled = true\nfilter = sshd\nlogpath = /var/log/auth.log\nmaxretry = 3\nbantime = 1h" > /etc/fail2ban/jail.d/sshd.conf
systemctl enable fail2ban && systemctl restart fail2ban

echo "clone project and variables substitution"
sudo -u ubuntu git clone --branch ${keeper_repository_branch} ${keeper_repository} $DIRECTORY
cd $DIRECTORY
cp templates/.vars.tmpl .vars
export SWAPPER_ADDRESS_KEY=${SWAPPER_ADDRESS_KEY}
export SWAPPER_ADDRESS=${SWAPPER_ADDRESS}
export CLOSER_ADDRESS_KEY=${CLOSER_ADDRESS_KEY}
export CLOSER_ADDRESS=${CLOSER_ADDRESS}
export DISTRIBUTOR_ADDRESS_KEY=${DISTRIBUTOR_ADDRESS_KEY}
export DISTRIBUTOR_ADDRESS=${DISTRIBUTOR_ADDRESS}
export DISTRIBUTOR_V2_ADDRESS_KEY=${DISTRIBUTOR_V2_ADDRESS_KEY}
export DISTRIBUTOR_V2_ADDRESS=${DISTRIBUTOR_V2_ADDRESS}
export HARVESTER_ADDRESS_KEY=${HARVESTER_ADDRESS_KEY}
export HARVESTER_ADDRESS=${HARVESTER_ADDRESS}
export REPORTER_ADDRESS_KEY=${REPORTER_ADDRESS_KEY}
export REPORTER_ADDRESS=${REPORTER_ADDRESS}
export REX_BANK_KEEPER_ADDRESS_KEY=${REX_BANK_KEEPER_ADDRESS_KEY}
export REX_BANK_KEEPER_ADDRESS=${REX_BANK_KEEPER_ADDRESS}
export airflow_password=${airflow_password}
export postgres_password=${postgres_password}
export gateway_uri=${gateway_uri}
export gateway_wss=${gateway_wss}
envsubst < templates/.vars.tmpl > .vars && chown ubuntu:ubuntu .vars

echo "Prepare database and run keeper"
su -l ubuntu -c "cd /home/ubuntu/ricochet-keeper; ./make.sh setup; ./make.sh deploy"
