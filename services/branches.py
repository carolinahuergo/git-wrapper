from os import environ
from git import Repo
from schemas.branch import Branch, Scope
import git

class BranchesService:

    def create_branch(self, branch_name):
        repo = Repo(environ.get('REPO_NAME'))
        repo.git.execute(['git', 'checkout', '-b', branch_name])

    def get_branches(self, scope):
        if scope == Scope.LOCAL:
            return self.get_local_branches()
        elif scope == Scope.REMOTE:
            return self.get_remote_branches()

    def get_local_branches(self):
        repo = Repo(environ.get('REPO_NAME'))
        branches = repo.heads
        return [ Branch(name=branch.name) for branch in branches ]

    def get_remote_branches(self):
        repo = Repo(environ.get('REPO_NAME'))
        branches = repo.remote().refs
        return [ Branch(name=branch.name) for branch in branches ]

    def get_current_branch(self):
        repo = Repo(environ.get('REPO_NAME'))
        return repo.active_branch

    def delete_branch(self, branch_name):
        repo = Repo(environ.get('REPO_NAME'))
        repo.git.branch("-d", branch_name)

    def checkout_branch(self, branch_name):
        repo = Repo(environ.get('REPO_NAME'))
        repo.git.checkout(branch_name)
        
    def change_branch_name(self, old_branch_name, new_branch_name):
        repo = Repo(environ.get('REPO_NAME'))
        repo.git.execute(['git', 'branch', '-m', old_branch_name, new_branch_name])