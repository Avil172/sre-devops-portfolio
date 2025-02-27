resource "aws_vpc" "comp-master-vpc" {
    cidr_block = "${var.aws_vpc_cidr}"
    instance_tenancy = "default"
    enable_dns_hostnames = true
    tags = {
        Name = "comp-master-vpc"
    }
}
