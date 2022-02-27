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

variable "address1" {
  type		= string
  sensitive = true
}

variable "key1" {
  type		= string
  sensitive = true
}

variable "address2" {
  type		= string
  sensitive = true
}

variable "key2" {
  type		= string
  sensitive = true
}

variable "address3" {
  type		= string
  sensitive = true
}

variable "key3" {
  type		= string
  sensitive = true
}

variable "address4" {
  type		= string
  sensitive = true
}

variable "key4" {
  type		= string
  sensitive = true
}

variable "address5" {
  type		= string
  sensitive = true
}

variable "key5" {
  type		= string
  sensitive = true
}

variable "address6" {
  type		= string
  sensitive = true
}

variable "key6" {
  type		= string
  sensitive = true
}

variable "address7" {
  type		= string
  sensitive = true
}

variable "key7" {
  type		= string
  sensitive = true
}

variable "gateway_uri" {
  type		= string
}

variable "gateway_wss" {
  type		= string
}

variable "airflow_password" {
  type		= string
  sensitive = true
}

variable "aws_public_key" {
  type		= string
  sensitive = true
}

variable "postgres_password" {
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
      cidr_block  = "0.0.0.0/0"
      description = "SSH" 
    },
    { 
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_block  = "0.0.0.0/0"
      description = "Web" 
    },
    { 
      from_port   = 5959
      to_port     = 5959
      protocol    = "tcp"
      cidr_block  = "0.0.0.0/0"
      description = "Keeper" 
    },
    { 
      from_port   = 3100
      to_port     = 3100
      protocol    = "tcp"
      cidr_block  = "0.0.0.0/0"
      description = "Monitoring" 
    },
    { 
      from_port   = 9080
      to_port     = 9080
      protocol    = "tcp"
       cidr_block  = "0.0.0.0/0"
      description = "Monitoring" 
    },
    { 
      from_port   = 9093
      to_port     = 9093
      protocol    = "tcp"
      cidr_block  = "0.0.0.0/0"
      description = "Monitoring" 
    },
    { 
      from_port   = 5555
      to_port     = 5555
      protocol    = "tcp"
      cidr_block  = "0.0.0.0/0"
      description = "Monitoring" 
    },
    { 
      from_port   = 9102
      to_port     = 9102
      protocol    = "tcp"
      cidr_block  = "0.0.0.0/0"
      description = "Monitoring" 
    },
  ]
}
