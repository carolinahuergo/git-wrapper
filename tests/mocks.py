import pytest
from pytest_mock import mocker


class MockObject:
    def __init__(self, title) -> None:
        self.title = title
    
@pytest.fixture
def git_mock():
    return mocker.patch('git.Repo')