import requests
import pytest



BASE_URL = "http://localhost:3000"

@pytest.fixture
def create_post():

    payload = {
            "title": "new",
            "views": 0
        }
    
    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    return str(response.json()["id"])

#TC-01   
def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0

    for post in posts:
        assert "id" in post
        assert "title" in post
        assert "views" in post
    
#TC-02    
def test_get_single_post(create_post):
    response = requests.get(f"{BASE_URL}/posts/"+create_post)

    assert response.status_code == 200

    post = response.json()

    assert isinstance(post, dict)
    assert str(post["id"]) == create_post
    
    
#TC-03
def test_get_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/0")

    assert response.status_code == 404
    
#TC-04    
def test_create_post():
    payload = {
        "title": "new",
        "views": 0
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201

    post = response.json()

    assert "id" in post
    assert isinstance(post["id"], int)
    assert post["title"] == "new"
    assert post["views"] == 0
    
#TC-05    
def test_update_post(create_post):
    payload = {
        "title": "updated",
        "views": 500
    }

    response = requests.put(
        f"{BASE_URL}/posts/"+ create_post,
        json=payload
    )

    assert response.status_code == 200

    post = response.json()

    assert str(post["id"]) == create_post
    assert post["title"] == "updated"
    assert post["views"] == 500
    
#TC-06
def test_patch_post(create_post):
    get_response = requests.get(f"{BASE_URL}/posts/"+create_post)

    assert get_response.status_code == 200

    original_post = get_response.json()
    original_title = original_post["title"]

    response = requests.patch(
        f"{BASE_URL}/posts/"+create_post,
        json={"views": 999}
    )

    assert response.status_code == 200

    updated_post = response.json()

    assert updated_post["id"] == original_post["id"]
    assert updated_post["title"] == original_title
    assert updated_post["views"] == 999
    
    
#TC-07
def test_delete_post(create_post):
    delete_response = requests.delete(
        f"{BASE_URL}/posts/"+create_post
    )

    assert delete_response.status_code in [200, 204]

    get_response = requests.get(
        f"{BASE_URL}/posts/"+create_post
    )

    assert get_response.status_code == 404