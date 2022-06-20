from fastapi import Depends
from daos.pullRequest import PullRequestDAO
from models.pullRequest import PullRequest
from github import Github
from os import environ
from schemas.pullRequest import PullRequestInput, PullRequestStatus
from services.branches import BranchesService

class PullRequestsService:

    def __init__(self, dao : PullRequestDAO = Depends()) -> None:
        self.dao = dao
        
    def save_pull_request(self, pull_request : PullRequestInput):
        g = Github(environ.get('GIT_USER_ACCESS_TOKEN'))
        repo = g.get_repo('carolinahuergo/git-wrapper')
        
        pull_request_created = repo.create_pull(
                title = pull_request.title, 
                body = pull_request.description,
                head = BranchesService().get_current_branch().name,
                base = pull_request.base)

        pull_request_to_save = PullRequest(
            title = pull_request.title, 
            description = pull_request.description, 
            number = pull_request_created.number, 
            status = PullRequestStatus.OPEN)

        self.dao.save(pull_request_to_save)

        return pull_request_created.number

    def merge_pull_request(self, pull_request_number):
        g = Github(environ.get('GIT_USER_ACCESS_TOKEN'))
        repo = g.get_repo('carolinahuergo/git-wrapper')
        repo.get_pull(pull_request_number).merge()
        self.dao.update(changes = {'status' : PullRequestStatus.MERGED})
