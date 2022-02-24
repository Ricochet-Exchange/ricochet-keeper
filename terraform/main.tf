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
resource "aws_security_group_rule" "sg_rules_keeper_in" {
  count = length(var.ingress_rules)

  type              = "ingress"
  from_port         = var.ingress_rules[count.index].from_port
  to_port           = var.ingress_rules[count.index].to_port
  protocol          = var.ingress_rules[count.index].protocol
  cidr_blocks       = [var.ingress_rules[count.index].cidr_block]
  description       = var.ingress_rules[count.index].description
  security_group_id = aws_security_group.sg_keeper.id
}

resource "aws_security_group_rule" "sg_rules_keeper_out" {
  type              = "egress"
  to_port           = 0
  protocol          = "-1"
  from_port         = 0
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg_keeper.id
}

resource "aws_instance" "keeper" {
  ami           		 = "ami-08ca3fed11864d6bb"
  instance_type 		 = "t2.medium"
  count         		 = 1
  vpc_security_group_ids = [
    aws_security_group.sg_keeper.id
  ]

  subnet_id     	      = aws_subnet.subnet_keeper.id
  associate_public_ip_address = true
  key_name                    = aws_key_pair.keeper.key_name
  user_data_base64            = base64encode(templatefile("./initscript.sh", {
    address1                   = var.keeper_wallet_address1
    key1                       = var.keeper_wallet_key1
    address2                   = var.keeper_wallet_address2
    key2                       = var.keeper_wallet_key2
    address3                   = var.keeper_wallet_address3
    key3                       = var.keeper_wallet_key3
    address4                   = var.keeper_wallet_address4
    key4                       = var.keeper_wallet_key4
    address5                   = var.keeper_wallet_address5
    key5                       = var.keeper_wallet_key5
    address6                   = var.keeper_wallet_address6
    key6                       = var.keeper_wallet_key6
    address7                   = var.keeper_wallet_address7
    key7                       = var.keeper_wallet_key7
    gateway-URI               = var.keeper_gateway_uri
    gateway-WSS               = var.keeper_gateway_wss
    a-strong-password-here    = var.keeper_password
    keeper_repository         = var.keeper_repository
    keeper_repository_branch  = var.keeper_repository_branch
  }))
}
