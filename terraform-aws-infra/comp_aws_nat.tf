resource "aws_nat_gateway" "comp-nat" {
    allocation_id = "${aws_eip.comp-eip.id}"
    subnet_id = "${aws_subnet.comp-master-public-subnet.id}"
    tags = {
        Name = "comp-nat"
    }
    depends_on = ["aws_internet_gateway.comp-igw"] 
}
