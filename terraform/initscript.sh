#!/bin/bash
set -xe
echo "Prepare install"
apt-get install -y ca-certificates curl gnupg lsb-release sudo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io
usermod -a -G docker ubuntu
sudo -u ubuntu mkdir -p /home/ubuntu/.docker/cli-plugins/
sudo -u ubuntu curl -SL https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -o /home/ubuntu/.docker/cli-plugins/docker-compose
chmod +x /home/ubuntu/.docker/cli-plugins/docker-compose
ln -s /home/ubuntu/.docker/cli-plugins/docker-compose /usr/bin/docker-compose



echo "clone project and deploy variables"
sudo -u ubuntu git clone --branch ${keeper_repository_branch} ${keeper_repository} /home/ubuntu/ricochet-keeper
cd /home/ubuntu/ricochet-keeper
sed -i .vars.backup 's/key1/${key1}/g'; 's/address1/${address1}/g'; 's/key2/${key2}/g'; 's/address2/${address2}/g'; 's/key3/${key3}/g'; 's/address3/${address3}/g'; 's/key4/${key4}/g'; 's/address4/${address4}/g'; 's/key5/${key5}/g'; 's/address5/${address5}/g'; 's/key6/${key6}/g'; 's/address6/${address6}/g'; 's/key7/${key7}/g'; 's/address7/${address7}/g'; 's/gateway-URI/${gateway-uri}/g'; 's/gateway-WSS/${gateway-wss}/g'; 's/a-strong-postgres-password/${airflow_password}/g'; 's/a-strong-postgres-password/${postgres_password}/g'; .vars


echo "Prepare database and run keeper"
su -l ubuntu -c "cd /home/ubuntu/ricochet-keeper; ./make.sh setup && ./make.sh deploy"
