from os import environ
from git import Repo
import re
from schemas.author import Author

NUMBER_OF_COMMITS_REGEX = '\d+|$' # first number is the number of commits from author
USERNAME_REGEX = r'\t(.*?) <' # the username is after a tab and before the bracket <
EMAIL_REGEX = r'<(.*?)>' # the email is inside brackets <>
class AuthorsService:

    def get_all_authors(self):
        repo = Repo(environ.get('REPO_NAME'))
        authors = repo.git.execute(['git', 'shortlog', '--summary', '--email', '--all'])
        return self._parse_authors(authors) if authors else []

    def get_authors_for_current_branch(self):
        repo = Repo(environ.get('REPO_NAME'))
        authors = repo.git.execute(['git', 'shortlog', '--summary', '--email'])
        return self._parse_authors(authors) if authors else []

    def _parse_authors(self, authors_to_parse: str):
        authors = []
        authors_to_parse = authors_to_parse.split(sep = '\n')
        for author in authors_to_parse:
            number_of_commits = int(re.search(NUMBER_OF_COMMITS_REGEX, author).group())
            username = re.search(USERNAME_REGEX, author).group(1)
            email = re.search(EMAIL_REGEX, author).group(1)
            authors.append(Author(username = username, email = email, number_of_commits = number_of_commits))
        return authors