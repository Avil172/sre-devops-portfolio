resource "aws_internet_gateway" "comp-igw" {
    vpc_id = "${aws_vpc.comp-master-vpc.id}"
    tags = {
        Name = "comp-igw"
    }
}
