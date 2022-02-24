variable "aws_access_key" {
  type      = string
  sensitive = true
}

variable "aws_secret_key" {
  type      = string
  sensitive = true
}

variable "aws_region" {
  type      = string
}

variable "keeper_repository" {
  type      = string
  default   = "master"
}

variable "keeper_repository_branch" {
  type      = string
  default   = "master"
}

variable "keeper_wallet_address" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_key" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_address1" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_key1" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_address2" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_key2" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_address3" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_key3" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_address4" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_key4" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_address5" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_key5" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_address6" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_key6" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_address7" {
  type		= string
  sensitive = true
}

variable "keeper_wallet_key7" {
  type		= string
  sensitive = true
}

variable "keeper_gateway_uri" {
  type		= string
}

variable "keeper_gateway_wss" {
  type		= string
}

variable "keeper_password" {
  type		= string
  sensitive = true
}

variable "aws_public_key" {
  type		= string
  sensitive = true
}
  
variable "ingress_rules" {
  type = list(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_block  = string
    description = string
  }))
  default = [
    { 
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_block  = "82.64.36.189/32"
      description = "SSH" 
    },
    { 
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_block  = "87.90.188.5/32"
      description = "SSH" 
    },
    { 
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_block  = "82.64.36.189/32"
      description = "Web" 
    },
    { 
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_block  = "87.90.188.5/32"
      description = "Web" 
    },
    { 
      from_port   = 5959
      to_port     = 5959
      protocol    = "tcp"
      cidr_block  = "87.90.188.5/32"
      description = "Keeper" 
    },
    { 
      from_port   = 5959
      to_port     = 5959
      protocol    = "tcp"
      cidr_block  = "82.64.36.189/32"
      description = "Keeper" 
    },
    { 
      from_port   = 3100
      to_port     = 3100
      protocol    = "tcp"
      cidr_block  = "87.90.188.5/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 3100
      to_port     = 3100
      protocol    = "tcp"
      cidr_block  = "82.64.36.189/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 9080
      to_port     = 9080
      protocol    = "tcp"
       cidr_block  = "87.90.188.5/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 9080
      to_port     = 9080
      protocol    = "tcp"
      cidr_block  = "82.64.36.189/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 9093
      to_port     = 9093
      protocol    = "tcp"
      cidr_block  = "87.90.188.5/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 9093
      to_port     = 9093
      protocol    = "tcp"
      cidr_block  = "82.64.36.189/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 5555
      to_port     = 5555
      protocol    = "tcp"
      cidr_block  = "87.90.188.5/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 5555
      to_port     = 5555
      protocol    = "tcp"
      cidr_block  = "82.64.36.189/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 9102
      to_port     = 9102
      protocol    = "tcp"
      cidr_block  = "87.90.188.5/32"
      description = "Monitoring" 
    },
    { 
      from_port   = 9102
      to_port     = 9102
      protocol    = "tcp"
      cidr_block  = "82.64.36.189/32"
      description = "Monitoring" 
    },
  ]
}
