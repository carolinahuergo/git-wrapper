from enum import Enum
from pydantic import BaseModel

class Scope(Enum):
    REMOTE = 'remote'
    LOCAL = 'local'
class Branch(BaseModel):
    name : str