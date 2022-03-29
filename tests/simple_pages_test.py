"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/page1">Git</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/oops">OOPs</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data


def test_request_page1(client):
    """This makes the Git page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git" in response.data


def test_request_page2(client):
    """This makes the Docker page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_page3(client):
    """This makes the Python/Flask page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data


def test_request_page4(client):
    """This makes the CI/CD page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Continuous Integration and Deployment" in response.data


def test_request_page5(client):
    """This makes the oops page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"Object Oriented Programming with Python" in response.data

def test_request_page6(client):
    """This makes the AAA Testing page"""
    response = client.get("/aaa_testing")
    assert response.status_code == 200
    assert b"AAA Testing" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page_n")
    assert response.status_code == 404
