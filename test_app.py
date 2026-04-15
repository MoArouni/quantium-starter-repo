import os
import pytest
from app import dash_app

# 1. Local Driver Fix
os.environ["PATH"] += os.pathsep + os.getcwd()

def test_header_exists(dash_duo):
    dash_duo.start_server(dash_app, port=8050)
    # If this succeeds, the element is present.
    dash_duo.wait_for_element("#header", timeout=10)

def test_visualization_exists(dash_duo):
    dash_duo.start_server(dash_app, port=8050)
    # We wait specifically for the graph to appear. 
    # Just waiting for it is enough to prove it exists.
    dash_duo.wait_for_element("#visualization", timeout=10)

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(dash_app, port=8050)
    dash_duo.wait_for_element("#region_picker", timeout=10)