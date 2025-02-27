resource "aws_vpn_connection" "comp-vpn" {
    vpn_gateway_id = "${aws_vpn_gateway.comp-vpgw.id}"
    customer_gateway_id = "${aws_customer_gateway.comp-cgw.id}"
    type = "ipsec.1"
    static_routes_only = true
}

resource "aws_vpn_connection_route" "comp-vpn-static-ip-prefix" {
    destination_cidr_block = "172.18.1.0/24"
    vpn_connection_id = "${aws_vpn_connection.comp-vpn.id}"
}
