resource "aws_customer_gateway" "comp-cgw" {
    bgp_asn = 65000
    ip_address = "182.72.8.182"
    type = "ipsec.1"
    tags = {
        Name = "comp-cgw"
    }
}
