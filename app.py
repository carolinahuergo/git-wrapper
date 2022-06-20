from fastapi import FastAPI
from git import GitCommandError
from github import GithubException
from controllers import authors, branches, commits, pullRequests
from dotenv import load_dotenv
from databases.sqlite import Base, engine
from utils.errors import git_command_error_exception_handler, github_exception_handler


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_exception_handler(GitCommandError, git_command_error_exception_handler)
app.add_exception_handler(GithubException, github_exception_handler)
app.include_router(commits.router)
app.include_router(branches.router)
app.include_router(authors.router)
app.include_router(pullRequests.router)

load_dotenv()