from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS

with Diagram("Simple AWS Architecture", show=False):
    lb = ELB("Load Balancer")
    web = EC2("Web Server")
    db = RDS("Database")

    lb >> web >> db
