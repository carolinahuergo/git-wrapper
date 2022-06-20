from os import environ
from git.repo import Repo
from dotenv import load_dotenv


load_dotenv()

repo = Repo.clone_from(environ.get('REPO_URL'), environ.get('REPO_DIRECTORY'))