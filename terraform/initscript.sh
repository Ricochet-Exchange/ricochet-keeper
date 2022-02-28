#!/bin/bash
set -xe
echo "Prepare install"
apt-get install -y ca-certificates curl gnupg lsb-release sudo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io
usermod -a -G docker ubuntu
export DOCKER_CONFIG=/home/ubuntu/.docker
sudo -u ubuntu mkdir -p $DOCKER_CONFIG/cli-plugins
sudo -u ubuntu curl -SL https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x /home/ubuntu/.docker/cli-plugins/docker-compose
ln -s /home/ubuntu/.docker/cli-plugins/docker-compose /usr/bin/docker-compose


echo "Fail2ban deployment"
apt-get install -y fail2ban
echo -e '/[sshd]/afilter = sshd\nlogpath = /var/log/auth.log\nmaxretry = 3\nbantime = 1h' /etc/fail2ban/jail.d/defaults-debian.conf

echo "clone project and variables substitution"
sudo -u ubuntu git clone --branch ${keeper_repository_branch} ${keeper_repository} /home/ubuntu/ricochet-keeper
cd /home/ubuntu/ricochet-keeper
echo ${key1}
envsubst < .vars

echo "Prepare database and run keeper"
su -l ubuntu -c "cd /home/ubuntu/ricochet-keeper; ./make.sh setup && ./make.sh deploy"
