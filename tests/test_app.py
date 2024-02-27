import os
import pytest
import requests_mock

from pathlib import Path

from news import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_app_works(client):
    """Validates that the application calls endpoints for rss feeds and returns a html page."""
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    test_data_path = current_path / "bbc-rss.xml"

    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, text=test_data_path.read_text())
    
        response = client.get("/")

        assert response.status_code == 200
        assert m.call_count == 7
