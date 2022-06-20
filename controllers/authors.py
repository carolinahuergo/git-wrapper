from fastapi import APIRouter, Depends, status
from typing import List
from schemas.author import Author
from services.authors import AuthorsService


router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)

@router.get("/", status_code = status.HTTP_200_OK, response_model=List[Author])
async def get_all_authors(service: AuthorsService = Depends()): 
    return service.get_all_authors()

@router.get("/currentBranch", status_code = status.HTTP_200_OK, response_model=List[Author])
async def get_authors_for_current_branch(service: AuthorsService = Depends()): 
    return service.get_authors_for_current_branch()
