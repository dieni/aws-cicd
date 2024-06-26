"""
Setup the basics before running the api tests
"""

import subprocess
import time

import pytest
import requests

START_SERVER_COMMAND = ["make", "run"]
SERVER_URL = "http://0.0.0.0:8000"  # Update the URL and port as needed


@pytest.fixture(scope="session", autouse=True)
def start_server():
    """Fixture to start the server before tests and stop it after."""
    # Start the server
    server_process = subprocess.Popen(START_SERVER_COMMAND)
    time.sleep(5)

    # Check if the server is up
    try:
        requests.get(SERVER_URL)
    except requests.exceptions.ConnectionError:
        server_process.terminate()
        raise RuntimeError("Server did not start")

    # Yield control to the tests
    yield

    # Stop the server after tests
    server_process.terminate()
    server_process.wait()
