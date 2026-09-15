import requests

BASE_URL = "http://localhost:3000"


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    
def test_post():
    payload = {"id": "1", "title": "Automated Post"}
    post_response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert post_response.status_code == 201
    
def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == "1"
    assert response.json()["title"] == "Automated Post"