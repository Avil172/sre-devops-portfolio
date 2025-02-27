data "aws_ami" "ubuntu" {
    most_recent = true

    filter {
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-*"]
    }

    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }

    filter {
        name = "sriov-net-support"
        values = ["simple"]
    }

    filter {
        name = "architecture"
        values = ["x86_64"]
    }

    owners = ["099720109477"]
}

resource "aws_instance" "xenial" {
    ami = "${data.aws_ami.ubuntu.id}"
    instance_type = "t2.micro"
    monitoring = true
    count = "1"
    key_name = "${var.aws_key_name}"
    subnet_id = "${aws_subnet.comp-master-private-subnet.id}"
    vpc_security_group_ids = ["aws_security_group.comp-private-sg"]
    tags{
        Name = "compsoft-DevOps${count.index + 1}"
    }
}
