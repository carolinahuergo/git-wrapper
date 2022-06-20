from fastapi import APIRouter, Depends, status
from typing import List
from schemas.commit import Commit, CommitInput
from services.commits import CommitsService


router = APIRouter(
    prefix="/commits",
    tags=["Commits"],
)

@router.get("/", status_code = status.HTTP_200_OK)
async def get_commits_for_all_branches_controller(service: CommitsService = Depends()): 
    return service.get_commits_for_all_branches()

@router.get("/{branch_name}", response_model = List[Commit], status_code = status.HTTP_200_OK)
async def get_commits_by_branch_controller(branch_name: str, service: CommitsService = Depends()):
    return service.get_commits_by_branch(branch_name)
    
@router.get("/{branch_name}/{hexsha}", response_model = Commit, status_code = status.HTTP_200_OK)
async def get_branch_commit_by_hexsha_controller(branch_name: str, hexsha: str, service: CommitsService = Depends()):
    return service.get_branch_commit_by_hexsha(branch_name, hexsha)

@router.post("/", status_code = status.HTTP_201_CREATED)
async def commit_controller(commit_input: CommitInput, service: CommitsService = Depends()):
    service.commit(commit_input)
