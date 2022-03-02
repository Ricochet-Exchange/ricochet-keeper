#!/bin/bash
set -xe
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
export key1=${key1}
export address1=${address1}
export key2=${key2}
export address2=${address2}
export key3=${key3}
export address3=${address3}
export key4=${key4}
export address4=${address4}
export key5=${key5}
export address5=${address5}
export key6=${key6}
export address6=${address6}
export key7=${key7}
export address7=${address7}
export airflow_password=${airflow_password}
export postgres_password=${postgres_password}
export gateway_uri=${gateway_uri}
export gateway_wss=${gateway_wss}
envsubst < templates/.vars.tmpl > .vars && chown ubuntu:ubuntu .vars

echo "Prepare database and run keeper"
su -l ubuntu -c "cd /home/ubuntu/ricochet-keeper; ./make.sh setup; ./make.sh deploy"
