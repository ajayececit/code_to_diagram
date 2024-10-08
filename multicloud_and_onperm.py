from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
from diagrams.gcp.compute import GCE
from diagrams.azure.compute import VM
from diagrams.onprem.compute import Server
from diagrams.onprem.client import User
from diagrams.generic.network import Firewall, Switch, Router
from diagrams.generic.storage import Storage  # Use generic storage instead of NAS

with Diagram("Multi-Cloud and On-Prem Architecture", show=False):

    # On-premise infrastructure
    with Cluster("On-Premise Data Center"):
        users = User("Users")
        firewall = Firewall("Firewall")
        router = Router("Router")
        switch = Switch("Switch")
        onprem_server = Server("Local Server")
        nas_storage = Storage("Storage")  # Generic storage replacing NAS

        users >> firewall >> router >> switch >> onprem_server
        onprem_server >> nas_storage

    # AWS infrastructure
    with Cluster("AWS Cloud"):
        aws_lb = ELB("Load Balancer")
        aws_ec2 = EC2("App Servers")
        aws_rds = RDS("Database")

        aws_lb >> aws_ec2 >> aws_rds

    # GCP infrastructure
    with Cluster("GCP Cloud"):
        gcp_gce = GCE("Compute Engine")
        gcp_storage = Storage("GCP Storage")

        gcp_gce >> gcp_storage

    # Azure infrastructure
    with Cluster("Azure Cloud"):
        azure_vm = VM("Virtual Machines")
        azure_storage = Storage("Azure Storage")

        azure_vm >> azure_storage

    # Connecting on-prem to cloud components via VPN
    router >> Edge(label="VPN") >> [aws_lb, gcp_gce, azure_vm]
