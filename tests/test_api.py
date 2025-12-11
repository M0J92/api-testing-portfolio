# tests/test_api.py
import pytest
from playwright.sync_api import APIRequestContext, Playwright

@pytest.fixture(scope="session")
def api_context(playwright):
    """Create an API request context for all tests"""
    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    request_context.dispose()


def test_get_single_user(api_context: APIRequestContext):
    """Test getting a single user from the API"""
    # Make a GET request to /users/1
    response = api_context.get("/users/1")
    
    # Check the response was successful (status code 200)
    assert response.ok
    
    # Get the JSON data from the response
    user = response.json()
    
    # Check the user has an id of 1
    assert user["id"] == 1
    
    # Check the user has a name
    assert "name" in user
    
    print(f"User name: {user['name']}")

def test_get_all_users(api_context: APIRequestContext):
    """Test getting all users"""
    response = api_context.get("/users")
    
    assert response.ok
    
    users = response.json()
    
    # Check we have a list
    assert isinstance(users, list)
    
    # Check we have 10 users
    assert len(users) == 10
    
def test_create_user(api_context: APIRequestContext):
    """Test creating a new user with POST"""
    # The data we want to send
    new_user = {
        "name": "Matt Jones",
        "username": "mattj",
        "email": "matt@example.com"
    }
    
    # Make a POST request to /users with our data
    response = api_context.post("/users", data=new_user)
    
    # Check it was successful (status 201 = created)
    assert response.status == 201
    
    # Get the created user from the response
    created_user = response.json()
    
    # Check the server gave us an ID
    assert "id" in created_user
    
    # Check our data was saved correctly
    assert created_user["name"] == "Matt Jones"
    assert created_user["username"] == "mattj"
    assert created_user["email"] == "matt@example.com"
    
    print(f"Created user with ID: {created_user['id']}")

def test_update_user(api_context: APIRequestContext):
    """Test updating a user with PUT"""
    # The complete updated user data
    updated_user = {
        "id": 1,
        "name": "Updated Name",
        "username": "updated_username",
        "email": "updated@example.com"
    }
    
    # Make a PUT request to /users/1 with updated data
    response = api_context.put("/users/1", data=updated_user)
    
    # Check it was successful (status 200 = OK)
    assert response.status == 200
    
    # Get the updated user from the response
    user = response.json()
    
    # Check the data was updated
    assert user["id"] == 1
    assert user["name"] == "Updated Name"
    assert user["username"] == "updated_username"
    assert user["email"] == "updated@example.com"
    
    print(f"Updated user {user['id']}: {user['name']}")

def test_partial_update_user(api_context: APIRequestContext):
    """Test partially updating a user with PATCH"""
    # Only the fields we want to update
    partial_update = {
        "name": "Partially Updated Name"
    }
    
    # Make a PATCH request to /users/1
    response = api_context.patch("/users/1", data=partial_update)
    
    # Check it was successful
    assert response.status == 200
    
    # Get the updated user
    user = response.json()
    
    # Check only the name was updated
    assert user["name"] == "Partially Updated Name"
    
    # The user should still have an id
    assert user["id"] == 1
    
    print(f"Partially updated user {user['id']}")


def test_delete_user(api_context: APIRequestContext):
    """Test deleting a user with DELETE"""
    # Make a DELETE request to /users/1
    response = api_context.delete("/users/1")
    
    # Check it was successful (status 200 = OK)
    assert response.status == 200
    
    print("User deleted successfully")

def test_get_users_with_query_params(api_context: APIRequestContext):
    """Test getting users with query parameters"""
    # Make a GET request with query parameters
    response = api_context.get("/users?id=1")
    
    # Check it was successful
    assert response.status == 200
    
    # Get the users (returns a list)
    users = response.json()
    
    # Should return a list with 1 user
    assert isinstance(users, list)
    assert len(users) == 1
    
    # The user should have id of 1
    assert users[0]["id"] == 1
    

    print(f"Found {len(users)} user(s) with id=1")

def test_get_nonexistent_user(api_context: APIRequestContext):
    """Test getting a user that doesn't exist (404 error)"""
    # Try to get user with ID 999 (doesn't exist)
    response = api_context.get("/users/999")
    
    # Check we got a 404 status
    assert response.status == 404
    
    print("Correctly received 404 for nonexistent user")

def test_user_response_structure(api_context: APIRequestContext):
    """Test that user response has all expected fields"""
    # Get a single user
    response = api_context.get("/users/1")
    
    assert response.status == 200
    
    user = response.json()
    
    # Check all expected fields exist
    expected_fields = ["id", "name", "username", "email", "address", "phone", "website", "company"]
    
    for field in expected_fields:
        assert field in user, f"Missing field: {field}"
    
    # Check that id is a number
    assert isinstance(user["id"], int)
    
    # Check that name is a string
    assert isinstance(user["name"], str)
    
    print(f"User has all {len(expected_fields)} expected fields")

def test_response_status_codes(api_context: APIRequestContext):
    """Test various response status codes"""
    # Test 200 OK - successful GET
    response = api_context.get("/users/1")
    assert response.status == 200
    
    # Test 201 Created - successful POST
    new_user = {"name": "Test User", "email": "test@example.com"}
    response = api_context.post("/users", data=new_user)
    assert response.status == 201
    
    # Test 404 Not Found - invalid endpoint
    response = api_context.get("/invalid-endpoint")
    assert response.status == 404
    
    print("All status codes verified correctly")