terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.2.0"
    }
  }
}

provider "aws" {
  access_key  = var.aws_access_key
  secret_key  = var.aws_secret_key
  region      = var.aws_region
}

# Define connect key
resource "aws_key_pair" "keeper" {
  key_name   	= "keeper"
  public_key	= var.aws_public_key
}

# Create vpc
resource "aws_vpc" "vpc_keeper" {
  cidr_block = "172.32.0.0/16"
  tags       = {
    Name = "Keeper VPC"
  }
}
# Create subnet
resource "aws_subnet" "subnet_keeper" {
  vpc_id     = aws_vpc.vpc_keeper.id
  cidr_block = "172.32.1.0/24"
  availability_zone = "eu-west-1a"

  tags = {
    Name = "Keeper subnet"
  }
}

# Create gateway
resource "aws_internet_gateway" "gw_keeper" {
  vpc_id = aws_vpc.vpc_keeper.id

  tags = {
    Name = "gw_keeper"
  }
}

# Create default route
resource "aws_route_table" "rtb_keeper" {
  vpc_id = aws_vpc.vpc_keeper.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw_keeper.id
  }

  tags = {
    Name = "rtb_keeper"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet_keeper.id
  route_table_id = aws_route_table.rtb_keeper.id
}

# Create security group
resource "aws_security_group" "sg_keeper" {
  name        = "sg_keeper"
  description = "Keeper security group"
  vpc_id      = aws_vpc.vpc_keeper.id

  tags = {
    Name = "Keeper security group"
  }
}

# Firewall rules
resource "aws_security_group_rule" "sg_rules_in_ssh" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = var.ingress_cidr_blocks_ssh
  description       = "SSH" 
  security_group_id = aws_security_group.sg_keeper.id
}

resource "aws_security_group_rule" "sg_rules_in_http" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  cidr_blocks       = var.ingress_cidr_blocks_web
  description       = "WEB" 
  security_group_id = aws_security_group.sg_keeper.id
}

resource "aws_security_group_rule" "sg_rules_in_https" {
  type              = "ingress"
  from_port         = 443
  to_port           = 443
  protocol          = "tcp"
  cidr_blocks       = var.ingress_cidr_blocks_web
  description       = "WEB" 
  security_group_id = aws_security_group.sg_keeper.id
}

resource "aws_security_group_rule" "sg_rules_in_keeper" {
  type              = "ingress"
  from_port         = 5959
  to_port           = 5959
  protocol          = "tcp"
  cidr_blocks       = var.ingress_cidr_blocks_keeper
  description       = "Keeper" 
  security_group_id = aws_security_group.sg_keeper.id
}

resource "aws_security_group_rule" "sg_rules_out" {
  type              = "egress"
  to_port           = 0
  protocol          = "-1"
  from_port         = 0
  cidr_blocks       = var.egress_cidr_blocks
  security_group_id = aws_security_group.sg_keeper.id
}

resource "aws_instance" "keeper" {
  ami           		 = "ami-08ca3fed11864d6bb"
  instance_type 		 = "t2.large"
  count         		 = 1
  vpc_security_group_ids = [
    aws_security_group.sg_keeper.id
  ]

  subnet_id     	         = aws_subnet.subnet_keeper.id
  associate_public_ip_address    = true
  key_name                       = aws_key_pair.keeper.key_name
  user_data_base64               = base64encode(templatefile("./initscript.sh", {
    SWAPPER_ADDRESS              = var.SWAPPER_ADDRESS
    SWAPPER_ADDRESS_KEY          = var.SWAPPER_ADDRESS_KEY
    CLOSER_ADDRESS               = var.CLOSER_ADDRESS
    CLOSER_ADDRESS_KEY           = var.CLOSER_ADDRESS_KEY
    DISTRIBUTOR_ADDRESS          = var.DISTRIBUTOR_ADDRESS
    DISTRIBUTOR_ADDRESS_KEY      = var.DISTRIBUTOR_ADDRESS_KEY
    DISTRIBUTOR_V2_ADDRESS       = var.DISTRIBUTOR_V2_ADDRESS
    DISTRIBUTOR_V2_ADDRESS_KEY   = var.DISTRIBUTOR_V2_ADDRESS_KEY
    HARVESTER_ADDRESS            = var.HARVESTER_ADDRESS
    HARVESTER_ADDRESS_KEY        = var.HARVESTER_ADDRESS_KEY
    REPORTER_ADDRESS             = var.REPORTER_ADDRESS
    REPORTER_ADDRESS_KEY         = var.REPORTER_ADDRESS_KEY
    REX_BANK_KEEPER_ADDRESS      = var.REX_BANK_KEEPER_ADDRESS
    REX_BANK_KEEPER_ADDRESS_KEY  = var.REX_BANK_KEEPER_ADDRESS_KEY
    gateway_uri                  = var.gateway_uri
    gateway_wss                = var.gateway_wss
    airflow_password           = var.airflow_password
    postgres_password          = var.postgres_password
    keeper_repository          = var.keeper_repository
    keeper_repository_branch   = var.keeper_repository_branch
  }))
}

output "ec2_global_ips" {
  value = ["${aws_instance.keeper.*.public_ip}"]
}
