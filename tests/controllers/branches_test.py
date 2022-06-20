from fastapi.testclient import TestClient
from app import app
from schemas.branch import Branch, Scope


client = TestClient(app)

mock_branch = Branch(name='test_branch')

def test_create_branch(mocker):
    mocker.patch('services.branches.BranchesService.create_branch')
    response = client.post("/branches/test_branch")
    assert response.status_code == 201

def test_get_branches(mocker):
    mocker.patch('services.branches.BranchesService.get_branches', return_value = [mock_branch])
    response = client.get(f"/branches/{Scope.LOCAL.value}")
    assert response.status_code == 200
    assert response.json() == [mock_branch]

# i'd continue adding tests for each controller but since its not a real project i'll stop here