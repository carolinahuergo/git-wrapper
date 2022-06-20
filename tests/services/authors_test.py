from schemas.author import Author
from services.authors import AuthorsService


def test_get_all_authors(mocker):
    mocker.patch('services.authors.Repo')
    mocked_parse_authors = mocker.patch('services.authors.AuthorsService._parse_authors')
    AuthorsService().get_all_authors()
    mocked_parse_authors.assert_called()

# i'd continue testing, for example, what happenens when there is no author.

def test__parse_authors(mocker):
    authors_to_parse = '11\tcarolinahuergo <carolinahhuergo@icloud.com>'
    authors = AuthorsService()._parse_authors(authors_to_parse)
    expected_author = Author(
        username = "carolinahuergo", 
        email = "carolinahhuergo@icloud.com", 
        number_of_commits = 11)
    assert authors[0] == expected_author