from fastapi import Depends
from sqlalchemy.orm import Session

from databases.sqlite import get_db
from models.pullRequest import PullRequest, PullRequestStatus


class PullRequestDAO:

    def __init__(self, db : Session = Depends(get_db)) -> None:
        self.db = db

    def save(self, pull_request):
        self.db.add(pull_request)
        self.db.commit()

    def update(self, pull_request_number : int, changes : dict):
        pull_request = PullRequest.query.filter_by(number = pull_request_number).first()
        pull_request.update(changes)
        self.db.commit()