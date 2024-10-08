from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS

with Diagram("AWS Architecture with Clustering", show=False):
    with Cluster("Web Tier"):
        lb = ELB("Load Balancer")
        web_servers = [EC2("Web 1"), EC2("Web 2")]

    with Cluster("Database Tier"):
        db_primary = RDS("Primary DB")
        db_replica = RDS("Replica DB")

    lb >> web_servers >> db_primary
    db_primary >> db_replica
