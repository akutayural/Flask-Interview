import pytest
from flask import Flask
import json
from project.interview import configure_routes


def test_post_route__success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/login'

    mock_request_data = {
        'email': 'demo@financialhouse.io',
        'password': 'cjaiU8CV '
    }

    response = client.post(url, data=mock_request_data)
    assert response.status_code == 200


def test_post_route__failure__bad_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/login'

    mock_request_data = {'email':'',
                        'password':''}

    response = client.post(url, data=json.dumps(mock_request_data))
    #response = response.json()
    assert response.status_code == 200
    #assert response.json()['status'] == 'DECLINED'


def test_post_route__success_for_getClient():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/getClient'

    #Token must be inserted cause it's valid for 10 mins! After login you are going to see the tokken at the browser and you can copy paste it.
    mock_request_headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDcsMTMyNCwxMzMxLDEzMzgsMTMzOSwxMzQxXSwidGltZXN0YW1wIjoxNjc1Mjc2MTEyfQ.Ix5v4GwP8_M2hzwQBdZjCZSv9rdDwMfPm9woZivgQU4'
    }

    mock_request_data = {
        'transactionId': '1-1444392550-1'
    }

    response = client.post(url, data=mock_request_data, headers=mock_request_headers)
    assert response.status_code == 200

def test_post_route__success_for_getTransaction():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/getTransaction'

    #Token must be inserted cause it's valid for 10 mins! After login you are going to see the tokken at the browser and you can copy paste it.
    mock_request_headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDcsMTMyNCwxMzMxLDEzMzgsMTMzOSwxMzQxXSwidGltZXN0YW1wIjoxNjc1Mjc2MTEyfQ.Ix5v4GwP8_M2hzwQBdZjCZSv9rdDwMfPm9woZivgQU4'
    }

    mock_request_data = {
        'transactionId': '1-1444392550-1'
    }

    response = client.post(url, data=mock_request_data, headers=mock_request_headers)
    assert response.status_code == 200


#/transactionQuery

def test_post_route__success_for_transactionQueryFirst():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/transactionQuery'

    #Token must be inserted cause it's valid for 10 mins! After login you are going to see the tokken at the browser and you can copy paste it.
    mock_request_headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDcsMTMyNCwxMzMxLDEzMzgsMTMzOSwxMzQxXSwidGltZXN0YW1wIjoxNjc1Mjc2MTEyfQ.Ix5v4GwP8_M2hzwQBdZjCZSv9rdDwMfPm9woZivgQU4'
    }

    mock_request_data = {}

    response = client.post(url, data=mock_request_data, headers=mock_request_headers)
    assert response.status_code == 200

def test_post_route__success_for_transactionQuerySecond():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/transactionQuery'

    #Token must be inserted cause it's valid for 10 mins! After login you are going to see the tokken at the browser and you can copy paste it.
    mock_request_headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDcsMTMyNCwxMzMxLDEzMzgsMTMzOSwxMzQxXSwidGltZXN0YW1wIjoxNjc1Mjc2MTEyfQ.Ix5v4GwP8_M2hzwQBdZjCZSv9rdDwMfPm9woZivgQU4'
    }

    mock_request_data = {
        'fromDate': '2015-07-01',
        'toDate': '2015-10-01'
    }

    response = client.post(url, data=mock_request_data, headers=mock_request_headers)
    assert response.status_code == 200

def test_post_route__success_for_transactionQueryThird():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/transactionQuery'

    #Token must be inserted cause it's valid for 10 mins!  After login you are going to see the tokken at the browser and you can copy paste it.
    mock_request_headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDcsMTMyNCwxMzMxLDEzMzgsMTMzOSwxMzQxXSwidGltZXN0YW1wIjoxNjc1Mjc2MTEyfQ.Ix5v4GwP8_M2hzwQBdZjCZSv9rdDwMfPm9woZivgQU4'
    }

    mock_request_data = {
        'fromDate': '2015-07-01',
        'toDate': '2015-10-01',
        'merchantId': '1',
        'acquirerId': '1'
    }

    response = client.post(url, data=mock_request_data, headers=mock_request_headers)
    assert response.status_code == 200

def test_post_route__success_for_transactionQueryFourth():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/transactionQuery'

    #Token must be inserted cause it's valid for 10 mins! After login you are going to see the tokken at the browser and you can copy paste it.
    mock_request_headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDcsMTMyNCwxMzMxLDEzMzgsMTMzOSwxMzQxXSwidGltZXN0YW1wIjoxNjc1Mjc2MTEyfQ.Ix5v4GwP8_M2hzwQBdZjCZSv9rdDwMfPm9woZivgQU4'
    }

    mock_request_data = {
        'fromDate': '2015-07-01',
        'toDate': '2015-10-01',
        'merchantId': '1',
        'acquirerId': '1',
        'status': 'APPROVED',
        'operation': 'DIRECT',
        'paymentMethod': 'CREDITCARD',
        'filterField': 'Reference No',
        'filterValue': '1-1568845-56',
        'page': '1'
    }

    response = client.post(url, data=mock_request_data, headers=mock_request_headers)
    assert response.status_code == 200

def test_post_route__success_for_transactionQueryFifth():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/transactionQuery'

    #Token must be inserted cause it's valid for 10 mins!  After login you are going to see the tokken at the browser and you can copy paste it.
    mock_request_headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDcsMTMyNCwxMzMxLDEzMzgsMTMzOSwxMzQxXSwidGltZXN0YW1wIjoxNjc1Mjc2MTEyfQ.Ix5v4GwP8_M2hzwQBdZjCZSv9rdDwMfPm9woZivgQU4'
    }

    mock_request_data = {
        'status': 'DECLINED',
        'operation': '3D',
        'errorCode': 'Invalid Transaction'
    }

    response = client.post(url, data=mock_request_data, headers=mock_request_headers)
    assert response.status_code == 200