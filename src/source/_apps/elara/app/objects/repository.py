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


    # Repository Properties
    _prop_own               = constants.RepoProps.OWNER.value
    _prop_repo              = constants.RepoProps.REPO.value
    _prop_vcs               = constants.RepoProps.VCS.value
    _prop_type              = constants.RepoProps.VCS_TYPE.value
    _prop_back              = constants.RepoProps.BACKENDS.value
    _prop_auth              = constants.RepoProps.AUTH.value
    _prop_head              = constants.RepoProps.HEADERS.value
    _prop_creds             = constants.RepoProps.CREDS.value
    ## Github Properties
    _prop_git               = constants.RepoProps.GITHUB.value
    _prop_api               = constants.RepoProps.API.value
    _prop_pr                = constants.RepoProps.PR.value
    _prop_com               = constants.RepoProps.COMMENTS.value
    _prop_pulls             = constants.RepoProps.PULLS.value
    _prop_files             = constants.RepoProps.FILES.value

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
        self.auth           = repository_config[self._prop_auth]
        self.backends       = repository_config[self._prop_back]
        self.src            = {
            self._prop_own  : owner,
            self._prop_repo : repository,
            self._prop_vcs  : repository_config[self._prop_type]
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

        if self.src[self._prop_vcs] == self._prop_git:
            return self.backends[self._prop_git][self._prop_api][self._prop_pr][endpoint]\
                            .format(**{ self._prop_pr: pr, **self.src})
        
        raise ValueError(
            f"Unsupported VCS: {self.src[self._prop_vcs]}")
    

    def _headers(self):
        """
        Returns the necessary headers for a request to the VCS backend. 

        .. note::

            Only ``github`` VCS is supported at this time.
            
        :returns: Dictionary of headers
        :rtype:  dict
        """

        if self.src[self._prop_vcs] == self._prop_git:
            if self.auth[self._prop_type] == "bearer":
                return {  
                    **self.backends[self._prop_git][self._prop_head],
                    "Authorization": "Bearer {token}".format(
                            token = self.auth[self._prop_creds]) 
                }
            
        raise ValueError("Error setting VCS Credentials")


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
                "name"      : self.src[self._prop_vcs],
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
                "name"      : self.src[self._prop_vcs],
                "body"      : res.json(),
                "status"    : "success"
            }
        }
    

    def vars(self) -> dict:
        """
        Retrieve VCS metadata, formatted for templating.
        """
        return { constants.TemplateVars.REPORT_REPO.value 
                            : self.src }


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
        url                 = self._pull(pr, self._prop_pulls)
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
        url                 = self._pull(pr, self._prop_com)
        body                = { "body": msg }
        return self._post(url, body)