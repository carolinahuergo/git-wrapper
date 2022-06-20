from pydantic import BaseModel

class Author(BaseModel):
    username : str
    email : str
    number_of_commits: int

    def __eq__(self, other):
        if self.username == other.username and self.email == other.email and self.number_of_commits == other.number_of_commits:
            return True
        else:
            return False