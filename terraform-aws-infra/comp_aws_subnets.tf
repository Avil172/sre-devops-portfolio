resource "aws_subnet" "comp-master-private-subnet" {
    vpc_id = "${aws_vpc.comp-master-vpc.id}"
    cidr_block = "173.19.1.0/24"
    map_public_ip_on_launch = false
    availability_zone = "ap-south-1a"
    tags = {
        Name = "comp-master-private-subnet"
    }
}

resource "aws_subnet" "comp-master-public-subnet" {
    vpc_id = "${aws_vpc.comp-master-vpc.id}"
    cidr_block = "173.19.2.0/24"
    map_public_ip_on_launch = true
    availability_zone = "ap-south-1b"
    tags = {
        Name = "comp-master-public-subnet"
    }
    depends_on = ["aws_internet_gateway.comp-igw"]
}

