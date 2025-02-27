variable "aws_access_key" {
    description = "AWS Access Key"
    default = "<access-key>"
}

variable "aws_secret_key" {
    description = "AWS Secret Key"
    default = "<secret>"
}

variable "aws_ssh_rsa" {
    description = "Public key of AWS"
    default = "ssh-rsa <rsa-key>"
}

variable "aws_key_name" {
    description = "Keyname for accessing AWS instances"
    default = "compconn"
}

variable "aws_region" {
    description = "AWS region of compsoft"
    default = "us-east-1"
}

variable "aws_vpc_cidr" {
    description = "The CIDR range of VPC for compsoft infrastructure"
    default = "173.19.0.0/16"
}





