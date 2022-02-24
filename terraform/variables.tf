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
