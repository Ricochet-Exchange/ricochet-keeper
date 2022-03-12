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

variable "address1" {
  type      = string
  sensitive = true
}

variable "key1" {
  type      = string
  sensitive = true
}

variable "address2" {
  type      = string
  sensitive = true
}

variable "key2" {
  type      = string
  sensitive = true
}

variable "address3" {
  type      = string
  sensitive = true
}

variable "key3" {
  type      = string
  sensitive = true
}

variable "address4" {
  type      = string
  sensitive = true
}

variable "key4" {
  type      = string
  sensitive = true
}

variable "address5" {
  type      = string
  sensitive = true
}

variable "key5" {
  type      = string
  sensitive = true
}

variable "address6" {
  type      = string
  sensitive = true
}

variable "key6" {
  type      = string
  sensitive = true
}

variable "address7" {
  type      = string
  sensitive = true
}

variable "key7" {
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

variable "ingress_cidr_blocks_monitoring" {
  type = list
  default = ["0.0.0.0/0"]
}
