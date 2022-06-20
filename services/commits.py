
from os import environ
from fastapi import HTTPException, status
from git import Repo
from utils.errors import ERROR_HEXSHA_NOT_FOUND
from schemas.commit import Commit

class CommitsService:

    def commit(self, commit):
        repo = Repo(environ.get('REPO_NAME'))
        repo.git.execute(['git', 'commit', '-m', commit.message])

    def get_commits_for_all_branches(self):
        repo = Repo(environ.get('REPO_NAME'))
        branches = repo.remote().refs
        commits_by_branch = {}
        for branch in branches:
            commits_by_branch[branch.name] = self.get_commits_by_branch(branch.name)
        return commits_by_branch

    def get_commits_by_branch(self, branch_name):
        repo = Repo(environ.get('REPO_NAME'))
        commits = []
        for commit in repo.iter_commits(branch_name):
            commits.append(Commit(
                    hexsha = commit.hexsha, 
                    author_name = commit.author.name,
                    committed_datetime = commit.committed_datetime,
                    message = commit.message 
                )
            )
        return commits

    def get_branch_commit_by_hexsha(self,branch_name, hexsha):
        commits = self.get_commits_by_branch(branch_name)
        for commit in commits:
            if commit.hexsha == hexsha:
                return commit
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = ERROR_HEXSHA_NOT_FOUND.format(hexsha))
    