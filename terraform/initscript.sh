#!/bin/bash
# Install docker
apt-get install -y ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io
usermod -a -G docker ubuntu

# Install docker-compose
curl -L "https://github.com/docker/compose/releases/download/2.2.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Get and configure repository 
sudo -u ubuntu git clone --branch monitoring https://github.com/samirsalem/ricochet-keeper.git /home/ubuntu/ricochet-keeper
cd /home/ubuntu/ricochet-keeper
sed -i -e 's/key/${key}/g' -e 's/address/${address}/g' -e 's/gateway-URI/${gateway-URI}/g' -e 's/gateway-WSS/${gateway-WSS}/g' -e 's/a-strong-password-here/${a-strong-password-here}/g' .vars

# Run keeper
sudo -u ubuntu ./make.sh setup
sudo -u ubuntu ./make.sh deploy
