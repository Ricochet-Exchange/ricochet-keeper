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
}

variable "keeper_repository_branch" {
  type      = string
  default   = "main"
}

variable "SWAPPER_ADDRESS" {
  type      = string
  sensitive = true
}

variable "SWAPPER_ADDRESS_KEY" {
  type      = string
  sensitive = true
}

variable "CLOSER_ADDRESS" {
  type      = string
  sensitive = true
}

variable "CLOSER_ADDRESS_KEY" {
  type      = string
  sensitive = true
}

variable "DISTRIBUTOR_ADDRESS" {
  type      = string
  sensitive = true
}

variable "DISTRIBUTOR_ADDRESS_KEY" {
  type      = string
  sensitive = true
}

variable "DISTRIBUTOR_V2_ADDRESS" {
  type      = string
  sensitive = true
}

variable "DISTRIBUTOR_V2_ADDRESS_KEY" {
  type      = string
  sensitive = true
}

variable "HARVESTER_ADDRESS" {
  type      = string
  sensitive = true
}

variable "HARVESTER_ADDRESS_KEY" {
  type      = string
  sensitive = true
}

variable "REPORTER_ADDRESS" {
  type      = string
  sensitive = true
}

variable "REPORTER_ADDRESS_KEY" {
  type      = string
  sensitive = true
}

variable "REX_BANK_KEEPER_ADDRESS" {
  type      = string
  sensitive = true
}

variable "REX_BANK_KEEPER_ADDRESS_KEY" {
  type      = string
  sensitive = true
}

variable "gateway_uri" {
  type      = string
}

variable "gateway_wss" {
  type      = string
}

variable "airflow_password" {
  type      = string
  sensitive = true
}

variable "aws_public_key" {
  type      = string
  sensitive = true
}

variable "postgres_password" {
  type      = string
  sensitive = true
}

variable "egress_cidr_blocks" {
  type = list
  default = ["0.0.0.0/0"]
}

variable "ingress_cidr_blocks_ssh" {
  type = list
  default = ["0.0.0.0/0"]
}

variable "ingress_cidr_blocks_web" {
  type = list
  default = ["0.0.0.0/0"]
}

variable "ingress_cidr_blocks_keeper" {
  type = list
  default = ["0.0.0.0/0"]
}
