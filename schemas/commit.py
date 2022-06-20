from datetime import datetime
from pydantic import BaseModel

class Commit(BaseModel):
    author_name : str
    hexsha : str
    committed_datetime : datetime
    message : str

class CommitInput(BaseModel):
    message : str