""" 
objects.repo
------------

Object for external Version Control System.

.. note::

    Only ``github`` VCS is supported at this time.    
"""
# Standard Library Modules 
import logging 
import typing

# External Modules
import requests

# Application Modules
import constants 
import decorators


logger                      = logging.getLogger(__name__)


class Repo:
    """
    Application repository. Class for managing interactions with a VCS backend. 
    """

    auth                    = None
    """Authentication configuration for VCS backend"""
    src                     = None
    """VCS source information"""
    backends                = None
    """Backend configurations"""


    def __init__(self, repository_config: dict, 
                 repository: str, owner: str) -> None:
        """
        Initialize Repository object.

        :param repo: Name of the VCS repository.
        :type repo: str
        :param owner: Username of the owner of the repository.
        :type owner: str
        :param repostiry_config: Repository configuration.
        :type repository_config: `dict`

        **Note**: `repository` must follow the schema,,

        .. code-block:: python


            repository_config       = {
                "VCS"               : "<github | bitbucket | codecommit>",
                "AUTH"              : {
                    "TYPE"          : "<bearer | oauth | etc. >",
                    "CREDS"         : "will change based on type."
                },
                "BACKENDS"          : {
                    "GITHUB"        : {
                        "HEADERS"   : {
                            # github vcs service headers
                        },
                        "API"       : {
                            # github vcs service endpoints
                        }
                    }
                }
            }
        
        .. note::

            Only ``github`` VCS is supported at this time.
            
        """
        owner_key           = constants.RepoProps.OWNER.value
        repo_key            = constants.RepoProps.REPO.value
        vcs_key             = constants.RepoProps.VCS.value
        vcs_type_key        = constants.RepoProps.VCS_TYPE.value
        backends_key        = constants.RepoProps.BACKENDS.value
        auth_key            = constants.RepoProps.AUTH.value

        self.auth           = repository_config[auth_key]
        self.backends       = repository_config[backends_key]
        self.src            = {
            owner_key       : owner,
            repo_key        : repository,
            vcs_key         : repository_config[vcs_type_key]
        }
    

    def _pull(self, pr: int, endpoint: constants.RepoProps) -> typing.Union[str | None]:
        """
        Returns the POST URL for the VCS REST API pull request endpoints.

        .. note::

            Only ``github`` VCS is supported at this time.
            
        :param pr: Pull request number for the POST.
        :type pr: `str`
        :param endpoint: Type of pull request endpoint.
        :type endpont: `constants.RepoProps.COMMENTS | constants.RepoProps.PULLS]`
        :returns: POST URL
        :rtype: `str`
        """
        vcs_key             = constants.RepoProps.VCS.value
        api_key             = constants.RepoProps.API.value
        pr_key              = constants.RepoProps.PR.value

        if self.src[vcs_key] == "github":
            github_key      = constants.RepoProps.GITHUB.value
            return self.backends[github_key][api_key][pr_key][endpoint]\
                            .format(**{ "pr": pr, **self.src})
        
        raise ValueError(
            f"Unsupported VCS: {self.src[vcs_key]}")
    

    def _headers(self):
        """
        Returns the necessary headers for a request to the VCS backend. 

        .. note::

            Only ``github`` VCS is supported at this time.
            
        :returns: Dictionary of headers
        :rtype:  dict
        """
        vcs_key             = constants.RepoProps.VCS.value
        github_key          = constants.RepoProps.GITHUB.value
        type_key            = constants.RepoProps.TYPE.value
        headers_key         = constants.RepoProps.HEADERS.value
        creds_key           = constants.RepoProps.CREDS.value

        if self.src[vcs_key] == "github":
            if self.auth[type_key] == "bearer":
                token       = self.auth[creds_key]

                return {  
                    **self.backends[github_key][headers_key],
                    "Authorization": f"Bearer {token}" 
                }
            
        raise ValueError(
            f"Unsupported auth type: {self.auth[type_key]} or VCS: {self.src[vcs_key]}"
        )


    # TODO: figure how to pass in self.src["vcs"] into decorator instead 
    #       of hard-coding the service name!
    @decorators.backoff(service="github")
    def _post(self, url: str, body: typing.Any) -> dict:
        """
        Make a HTTP post to a VCS backend. 

        :param url: URL of the request.
        :type url: `str`
        :param body: Body of the request.
        :type body: `typing.Any`
        :returns: Dictionary containing VCS response.
        :rtype: `dict`
        """
        logger.info(f"Making HTTP POST Request to {url}")

        res                 = requests.post(
            url             = url, 
            headers         = self._headers(), 
            json            = body
        )
        logger.debug(res)
        res.raise_for_status()
        return {
            "service": {
                "name"      : self.src[constants.RepoProps.VCS.value],
                "body"      : res.json(),
                "status"    : "success"
            }
        }
    

    # TODO: figure how to pass in self.src["vcs"] into decorator instead 
    #       of hard-coding the service name!          
    @decorators.backoff(service = "github")
    def _get(self, url: str) -> dict:
        """
        Make a HTTP get to a VCS backend. 

        :param url: URL of the request.
        :type url: `str`
        """
        logger.info(f"Making HTTP GET Request to {url}")
        res                 = requests.get(
            url             = url, 
            headers         = self._headers()
        )
        logger.debug(res)
        res.raise_for_status()
        return {
            "service":      {
                "name"      : self.src[constants.RepoProps.VCS.value],
                "body"      : res.json(),
                "status"    : "success"
            }
        }
    

    def vars(self) -> dict:
        """
        Retrieve VCS metadata, formatted for templating.
        """
        return { "repository" : self.src }


    def pulls(self, pr: str) -> dict:
        """
        List the files in a pull request diff.

        - **Github**: `Github REST API Docs: Pull Request Files <https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests-files>`
        """
        url                 = self._pull(
            pr              = pr,
            endpoint        = constants.RepoProps.FILES.value
        )  
        res                 = self._get(url)
        files               = []
        if res and res.get("service").get("status") == "success":
            for f in res.get("service").get("body"):
                files.append({
                    "file"  : f.get("filename"),
                    "sha"   : f.get("sha")
                })
        return files


    def files(self, pr: str, bodies: list) -> list:
        """
        Posts a comment to a pull request file on the VCS backend. Links below detail the specific VCS provider endpoints,

        - **Github**: `Github REST API Docs: Pull Request COmments <https://docs.github.com/en/rest/pulls/comments?apiVersion=2022-11-28#create-a-review-comment-for-a-pull-request>

        .. important::

            This is different than the `self.comment` function. This endpoint will target specific files.
            
        .. note::

            Only ``github`` VCS is supported at this time.

        The `bodies` parameter must follow the following schema,

        .. code-block:: python

            bodies      = [{
                "path"  : "path of file"
                "msg    : "message to post"
            }]

        :param pr: Pull request number on which to comment.
        :type pr: `str`,
        :param bodies: List of request bodies to post.
        :type bodies: `list`
        :returns: List of VCS responses.
        :rtype: `list`
        """
        files               = self.pulls(pr)
        url                 = self._pull(pr, constants.RepoProps.PULLS.value)
        paths               = [ b["path"] for b in bodies ]
        res                 = []

        for f in files:
            for p in paths:
                if f.get('file').endswith(p):
                    body    = {
                        "body": bodies[paths.index(p)],
                        "path": f.get("file"),
                        "commit_id": f.get("sha"),
                        "line": 1
                    }
                    res.append(self._post(url,body))
                    break 
        return res


    def comment(self, msg: str, pr: str) -> dict:
        """
        Post a comment to a pull request on the VCS backend. Links below detail the specific VCS provider endpoints,

        - **Github**: `Github REST API Docs: Issue Comments <https://docs.github.com/en/rest/issues/comments?apiVersion=2022-11-28#create-an-issue-comment>

        .. important::

            Github treats pull requests as issues. Posting to an Pull Request issue creates a comment on the main thread of the pull request. 

        .. note::

            Only ``github`` VCS is supported at this time.

        :param msg: Comment to post.
        :type msg: `str`
        :param pr: Pull request number on which to comment.
        :type pr: `str`
        """
        url                 = self._pull(pr,constants.RepoProps.COMMENTS.value)
        body                = { "body": msg}
        return self._post(url, body)