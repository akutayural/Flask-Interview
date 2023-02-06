import pytest
from flask import Flask
import json
from interview import login


def test_post_route__success():
    app = Flask(__name__)
    client = app.test_client()
    url = '/login'

    mock_request_data = {
        'email': 'demo@financialhouse.io',
        'password': 'cjaiU8CV '
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 200
