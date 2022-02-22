terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.2.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_key_pair" "keeper" {
  key_name   = "keeper"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDL8mnoz4nH2YPrbOUr+Fw34nAcwEwJX8mEvOQthd9wn7B+HjCuHgnaA4seFQ0B5VRQPozl9dJcaTkq985mbwY3WKvSap8cMOjwOo1qayLo6Vdn889C2N5F5MbCXr2H2MuRDsYemAWhavslJ+jEJgpjFCieSrDh55mVbvMWno7o3MBv/Po5STmfpo1oZfCMDoWcXMiHLQv5Y5LkdoO6BtJDnCVjooWHCI74B0As1crdN+8bn34j+C29tZtWYARuVWgW+1vRUIy6W+7ZxdOL8FncB7AJ2JyfkyEh05Gnq63NMzvoEgJQcr7g10j/AaH1qdk/ju6k/vt4QNfGc/zlYpOFMdvQTnUz+c09vhJMIn46pZhgJuaY+vhvhnbpuJNfOV/uKZM5PtjBbKNHV8X4rbE+bSC1XwPP21puUtFizJceCWFKZ+B1vs7GsZJTWdjygDXFInyCxfj7boZIPdoceAziaalL3SX1Y8B/eE0O41yyTTo2+aqluw9H+D/KKiowOLM="
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

resource "aws_security_group" "sg_keeper" {
  name        = "sg_keeper"
  description = "Keeper security group"
  vpc_id      = aws_vpc.vpc_keeper.id

  tags = {
    Name = "Keeper security group"
  }
}

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
  cidr_blocks       = [aws_vpc.vpc_keeper.cidr_block]
  security_group_id = aws_security_group.sg_keeper.id
}

resource "aws_network_interface" "iface_keeper" {
  subnet_id   = aws_subnet.subnet_keeper.id
}

resource "aws_instance" "keeper" {
  ami           = "ami-08ca3fed11864d6bb"
  instance_type = "t2.medium"
  count         = 1
  vpc_security_group_ids = [
    aws_security_group.sg_keeper.id
  ]

  subnet_id     = aws_subnet.subnet_keeper.id
  associate_public_ip_address = true
  key_name = aws_key_pair.keeper.key_name
  user_data = <<EOF
#!/bin/bash
EOF
}
