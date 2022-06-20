from fastapi import APIRouter, Depends, status
from sqlalchemy import Integer
from models.pullRequest import PullRequestInput, PullRequestResponse
from services.pullRequests import PullRequestsService


router = APIRouter(
    prefix="/pullRequests",
    tags=["Pull Requests"],
)

@router.post("/", status_code = status.HTTP_200_OK, response_model = PullRequestResponse)
async def save_pull_requests_controller(pull_request : PullRequestInput, service : PullRequestsService = Depends()):
    number = service.save_pull_request(pull_request)
    return PullRequestResponse(number = number)

@router.patch("/{pull_request_number}", status_code = status.HTTP_204_NO_CONTENT)
async def save_pull_requests_controller(pull_request_number : int, service : PullRequestsService = Depends()):
    service.merge_pull_request(pull_request_number)