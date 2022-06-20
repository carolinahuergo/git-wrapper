from fastapi.testclient import TestClient
from app import app
from schemas.author import Author

client = TestClient(app)

mock_author = Author(
    username = "carolina",
    email = "carolinahhuergo@icloud.com",
    number_of_commits = 10
)

def test_get_all_authors(mocker):
    mocker.patch('services.authors.AuthorsService.get_all_authors', return_value = [mock_author])
    response = client.get("/authors")
    assert response.status_code == 200
    assert Author(**response.json()[0]) == mock_author

def test_get_authors_for_current_branch(mocker):
    mocker.patch('services.authors.AuthorsService.get_authors_for_current_branch', return_value = [mock_author])
    response = client.get("/authors/currentBranch")
    assert response.status_code == 200
    assert Author(**response.json()[0]) == mock_author