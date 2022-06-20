import logging
from fastapi import Request, status
from fastapi.responses import JSONResponse
from git import GitCommandError
from github import GithubException

ERROR_BRANCH_NOT_FOUND = 'The branch was not found.'
ERROR_EXISTING_BRANCH = 'The branch already exists.'
ERROR_DELETE_CURRENT_BRANCH = 'Cannot delete current branch.'
ERROR_HEXSHA_NOT_FOUND = 'The hexsha was not found.'
ERROR_GENERIC = 'Internal error'
ERROR_BAD_COMMAND = 'There is an error on the git request: {}'
ERROR_NOTHING_TO_COMMIT = 'Cannot commit. Nothing to commit.'
ERROR_NOTHING_ADDED_TO_COMMIT = 'Cannot commit. Nothing added to commit but untracked files present.'

async def git_command_error_exception_handler(request: Request, exception: GitCommandError):
    logging.error(f"GitCommandError: \n {exception.stderr} {exception.stdout}")
    if isNothingToCommitError(exception):
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content = {'message': ERROR_NOTHING_TO_COMMIT})
    if isBranchNotFoundError(exception):
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND, content = {'message': ERROR_BRANCH_NOT_FOUND})
    if isCurrentBranchBeingDeletedError(exception):
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content = {'message': ERROR_DELETE_CURRENT_BRANCH})
    if isBranchAlreadyExistsError(exception):
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content = {'message': ERROR_EXISTING_BRANCH})
    if isNothingAddedToCommitError(exception):
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content = {'message': ERROR_NOTHING_ADDED_TO_COMMIT})
    return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, 
                        content = {'message': ERROR_BAD_COMMAND.format(getErrorMessageFromGitCommandError(exception))})

async def github_exception_handler(request: Request, exception: GithubException):
    message = exception.data['message']
    try:
        message += f" : {exception.data['errors'][0]['message']}"
    except:
        pass
    logging.error(f"GithubException: \n Error : {message}")
    return JSONResponse(status_code = exception.status,
                        content = {'message': message})

def isBranchAlreadyExistsError(exception):
    return 'a branch named' in exception.stderr and 'already exists' in exception.stderr

def isCurrentBranchBeingDeletedError(exception):
    return 'checked out' in exception.stderr

def isBranchNotFoundError(exception):
    return 'not found' in exception.stderr

def isNothingToCommitError(exception):
    return 'nothing to commit' in exception.stdout

def isNothingAddedToCommitError(exception):
    return 'nothing added to commit but untracked files present' in exception.stdout

def getErrorMessageFromGitCommandError(exception):
    return exception.stdout if exception.stdout > exception.stderr else exception.stderr