from enum import Enum
from pydantic import BaseModel

class PullRequestStatus(str, Enum):
    OPEN = 'Open'
    MERGED = 'Merged'

class PullRequestInput(BaseModel):
    title : str
    description : str
    base : str

class PullRequestResponse(BaseModel):
    number : int

