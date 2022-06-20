from enum import Enum
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as SQLEnum
from databases.sqlite import Base
from schemas.pullRequest import PullRequestStatus

class PullRequest(Base):

    __tablename__ = "pullrequests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(SQLEnum(PullRequestStatus), default = PullRequestStatus.OPEN)
    number = Column(Integer)

