from diagrams import Diagram
from diagrams.custom import Custom

# Create a diagram with a custom service using a local image
with Diagram("Custom Service Architecture - Local Icon", show=False):
    custom_service = Custom("My Custom Service", "./custom_icon.png")
