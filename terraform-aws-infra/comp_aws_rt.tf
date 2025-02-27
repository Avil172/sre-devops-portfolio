resource "aws_route_table" "comp-public-subnet-rt" {
    vpc_id = "${aws_vpc.comp-master-vpc.id}"
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = "${aws_internet_gateway.comp-igw.id}"
    }
    tags = {
        Name = "comp-public-subnet-rt"
    }
}

resource "aws_route_table" "comp-private-subnet-rt" {
    vpc_id = "${aws_vpc.comp-master-vpc.id}"
    route {
        cidr_block = "0.0.0.0/0"
        nat_gateway_id = "${aws_nat_gateway.comp-nat.id}"
    }
    route {
        cidr_block = "172.18.1.0/24"
        gateway_id = "${aws_vpn_gateway.comp-vpgw.id}"
    }
    tags = {
        Name = "comp-private-subnet-rt"
    }
}

