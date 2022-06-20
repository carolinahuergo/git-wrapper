from typing import List
from fastapi import APIRouter, Depends, status, Response
from schemas.branch import Branch, Scope
from services.branches import BranchesService

router = APIRouter(
    prefix="/branches",
    tags=["Branches"],
)

@router.post("/{branch_name}", status_code = status.HTTP_201_CREATED)
async def create_branch(branch_name: str, service: BranchesService = Depends()):
    service.create_branch(branch_name)

@router.get("/{scope}", status_code = status.HTTP_200_OK, response_model = List[Branch])
async def get_branches(scope: Scope, service: BranchesService = Depends()): 
    return service.get_branches(scope)

@router.get("/checkout/{branch_name}")
async def checkout_branch(branch_name: str, service: BranchesService = Depends()):
    service.checkout_branch(branch_name)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/{old_branch_name}')
async def change_branch_name(old_branch_name: str, new_branch: Branch, service: BranchesService = Depends()):
    service.change_branch_name(old_branch_name, new_branch.name)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete("/{branch_name}")
async def delete_branch(branch_name: str, service: BranchesService = Depends()):
    service.delete_branch(branch_name)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
