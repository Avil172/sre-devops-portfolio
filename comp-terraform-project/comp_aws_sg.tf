resource "aws_security_group" "comp-public-sg" {
    name = "comp-public-sg"
    description = "Security group rules for Public subnet"
    vpc_id = "${aws_vpc.comp-master-vpc.id}"
    ingress {
        from_port = 22
        protocol = "tcp"
        to_port = 22
        cidr_blocks = ["182.72.8.182/32"]
        description = "SSH access to this node"
    }
    
    egress {
        from_port = 0
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_security_group" "comp-private-sg" {
    name = "comp-private-sg"
    description = "Security group rules for Private subnet"
    vpc_id = "${aws_vpc.comp-master-vpc.id}"
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "SSH access to this node- AWS"
    }
    
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["173.19.2.0/24"]
        description = "SSH access to this node- on-prem"
    }

    ingress {
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for Jenkins master- AWS"
    }
    
    ingress {
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for Jenkins master- on-prem"
    }

    ingress {
        from_port = 8081
        to_port = 8081
        protocol = "tcp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for Jenkins agent- AWS"
    }
    
    ingress {
        from_port = 8081
        to_port = 8081
        protocol = "tcp"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for Jenkins agent- On-prem"
    }

    ingress {
        from_port = 9043
        to_port = 9043
        protocol = "tcp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for Nexus Sonatype Registry- AWS"
    }
    
    ingress {
        from_port = 9043
        to_port = 9043
        protocol = "tcp"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for Nexus Sonatype Registry- On-prem"
    }

    ingress {
        from_port = 9000
        to_port = 9000
        protocol = "tcp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for SonarQube Server- AWS"
    }
    
    ingress {
        from_port = 9000
        to_port = 9000
        protocol = "tcp"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for SonarQube Server- on-prem"
    }

    ingress {
        from_port = 3389
        to_port = 3389
        protocol = "rdp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for Windows based Jenkins Agent- AWS"
    }
    
    ingress {
        from_port = 3389
        to_port = 3389
        protocol = "rdp"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for Windows based Jenkins agent- On-Prem1"
    }
    
    ingress {
        from_port = 3389
        to_port = 3389
        protocol = "rdp"
        cidr_blocks = ["173.19.1.43/32"]
        description = "Port opening for Windows based Jenkins agent- On-Prem2"
    }
    
    ingress {
        from_port = 5432
        to_port = 5432
        protocol = "tcp"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for PostgreSQL- On-Prem"
    }
    
    ingress {
        from_port = 5432
        to_port = 5432
        protocol = "tcp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for PostgreSQL- AWS"
    }
    
    ingress {
        from_port = 443
        to_port = 443
        protocol = "https"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for HTTPS access- AWS"
    }
    
    ingress {
        from_port = 443
        to_port = 443
        protocol = "https"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for HTTPS access- On-Prem"
    }
    
    ingress {
        from_port = 8172
        to_port = 8172
        protocol = "tcp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for MSDeploy- AWS"
    }
    
    ingress {
        from_port = 8172
        to_port = 8172
        protocol = "tcp"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for MSDeploy- On-Prem"
    }
    
    ingress {
        from_port = 80
        to_port = 80
        protocol = "http"
        cidr_blocks = ["172.18.1.0/24"]
        description = "Port opening for HTTP access- AWS"
    }
    
    ingress {
        from_port = 80
        to_port = 80
        protocol = "http"
        cidr_blocks = ["173.19.2.0/24"]
        description = "Port opening for HTTP access- On-prem"
    }
    
    ingress {
        from_port = 8
        to_port = 0
        protocol = "icmp"
        cidr_blocks = ["172.18.1.0/24"]
        description = "ICMP protocol for AWS"
    }
    
    ingress {
        from_port = 8
        to_port = 0
        protocol = "icmp"
        self = true
        cidr_blocks = ["172.18.1.0/24"]
        description = "ICMP protocol for AWS SG"
    }
    
    egress {
        from_port = 0
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}

