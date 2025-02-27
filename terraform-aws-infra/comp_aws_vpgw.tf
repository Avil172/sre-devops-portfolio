resource "aws_vpn_gateway" "comp-vpgw" {
    vpc_id = "${aws_vpc.comp-master-vpc.id}"
    tags = {
        Name = "comp-vpgw"
    }
}
