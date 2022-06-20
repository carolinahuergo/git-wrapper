from fastapi import APIRouter, Depends, status, Response
from schemas.pullRequest import PullRequestInput, PullRequestResponse
from services.pullRequests import PullRequestsService


router = APIRouter(
    prefix="/pullRequests",
    tags=["Pull Requests"],
)

@router.post("/", status_code = status.HTTP_200_OK, response_model = PullRequestResponse)
async def save_pull_requests(pull_request : PullRequestInput, service : PullRequestsService = Depends()):
    number = service.save_pull_request(pull_request)
    return PullRequestResponse(number = number)

@router.patch("/{pull_request_number}")
async def merge_pull_request(pull_request_number : int, service : PullRequestsService = Depends()):
    service.merge_pull_request(pull_request_number)
    return Response(status_code=status.HTTP_204_NO_CONTENT)