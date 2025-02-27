resource "aws_eip" "comp-eip" {
    vpc = true
    depends_on = ["aws_internet_gateway.comp-igw"]
    tags = {
        Name = "comp-eip"
    }
}
