""" 
objects.repo
------------

Object for external Version Control System. 
"""
# Standard Library Modules 
import logging 
import time
import traceback
import typing

# External Modules
import requests

# Application Modules
import constants 

logger = logging.getLogger(__name__)


class Repo:
    """
    Application repository. Class for managing interactions with a VCS backend. 
    """

    auth                                        = None
    """Authentication configuration for VCS backend"""
    src                                         = None
    """VCS source information"""
    backends                                    = None
    """Backend configurations"""


    def __init__(self,
        repository_config                       : dict,
        repository                              : str, 
        owner                                   : str,
    ):
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


            repository_config               = {
                "VCS"                       : "<github | bitbucket | codecommit>",
                "AUTH"                      : {
                    "TYPE"                  : "<bearer | oauth | etc. >",
                    "CREDS"                 : "will change based on type."
                },
                "BACKENDS"                  : {
                    "GITHUB"                : {
                        "HEADERS"           : {
                            # github vcs service headers
                        },
                        "API"               : {
                            # github vcs service endpoints
                        }
                    }
                }
            }
        
        .. note::

            Only ``github`` VCS is supported at this time.
            
        """
        self.auth                               = repository_config[
            constants.RepoProps.AUTH.value
        ]
        self.backends                           = repository_config[
            constants.RepoProps.BACKENDS.value
        ]
        self.src                                = {
            constants.RepoProps.OWNER.value     : owner,
            constants.RepoProps.REPO.value      : repository,
            constants.RepoProps.VCS.value       : repository_config[
                constants.RepoProps.VCS_TYPE.value
            ]
        }


    @staticmethod
    def _service(svc: typing.Any)               -> dict:
        return { "service": svc }
    

    def _pull(self, 
        num                                     : int,
        endpoint                                : constants.RepoProps
    )                                           -> typing.Union[str | None]:
        """
        Returns the POST URL for the VCS REST API pull request endpoints.

        .. note::

            Only ``github`` VCS is supported at this time.
            
        :param num: Pull request number for the POST.
        :type num: `str`
        :param endpoint: Type of pull request endpoint.
        :type endpont: `constants.RepoProps.COMMENTS | constants.RepoProps.PULLS]`
        :returns: POST URL
        :rtype: `str`
        """
        if self.src[constants.RepoProps.VCS.value] == "github":

            return self.backends[constants.RepoProps.GITHUB.value][
                constants.RepoProps.API.value][constants.RepoProps.PR.value
            ][endpoint].format(**{
                "pr": num, 
                **self.src
            })
        
        raise ValueError(f"Unsupported VCS: {self.src[constants.RepoProps.VCS.value ]}")
    

    def _headers(self):
        """
        Returns the necessary headers for a request to the VCS backend. 

        .. note::

            Only ``github`` VCS is supported at this time.
            
        :returns: Dictionary of headers
        :rtype:  dict
        """
        if self.src[constants.RepoProps.VCS.value] == "github":
            if self.auth[constants. RepoProps.TYPE.value] == "bearer":
                token = self.auth[constants.RepoProps.CREDS.value]

                return {
                    "Authorization": f"Bearer {token}", 
                    **self.backends[constants.RepoProps.GITHUB.value
                                    ][constants.RepoProps.HEADERS.value]
                }
            
        raise ValueError(
            f"Unsupported auth type: {self.auth[
                constants.RepoProps.TYPE.value]} or VCS: {self.src[constants.RepoProps.VCS.value]}"
        )


    def _request(self,
        url                                     : str,
        body                                    : typing.Any,
        max_retries                             : int = 3
    )                                           -> dict:
        """
        Make a HTTP call to a VCS backend.

        :param 
        """
        for attempt in range(max_retries):
            try:
                logger.debug(f"Making HTTP call to {url}")

                res                                 = requests.post(
                    url                             = url, 
                    headers                         = self._headers(), 
                    json                            = body
                )
                logger.debug(res)
                res.raise_for_status()
                
                return self._service({
                    "name"                          : self.src[constants.RepoProps.VCS.value],
                    "body"                          : res.json(),
                    "status"                        : "success"
                })

            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    wait                            = 2 ** attempt
                    logger.warning(f"Request failed, retrying in {wait} seconds:\n\n{e}")
                    time.sleep(wait)
                else:
                    logger.error(f"Request to {self.src[
                    constants.RepoProps.VCS.value]} failed after {max_retries} attempts:\n\n{e}\n\n{traceback.print_exc()}")
                    return self._service({
                        "name"                          : self.src[constants.RepoProps.VCS.value],
                        "body"                          : str(e),
                        "status"                        : "failure"
                    })
            
            except Exception as e:
                logger.error(f"An unexpected error occurred:\n\n{e}\n\n{traceback.print_exc()}")
                return self._service({
                    "name"                          : self.src[constants.RepoProps.VCS.value],
                    "body"                          : str(e),
                    "status"                        : "failure"
                })
        
    def vars(self)                              -> dict:
        """
        Retrieve VCS metadata, formatted for templating.
        """
        return {
            "repository"                        : self.src
        }


    def file(self,
        msg                                     : str,
        pr                                      : str,
        commit                                  : str,
        path                                    : str,
    )                                           -> dict:
        """
        Posts a comment to a pull request file on the VCS backend. Links below detail the specific VCS provider endpoints,

        - **Github**: `Github REST API Docs: Pull Request COmments <https://docs.github.com/en/rest/pulls/comments?apiVersion=2022-11-28#create-a-review-comment-for-a-pull-request>

        .. important::

            This is different than the `self.comment` function. This endpoint will target specific files.
            
        .. note::

            Only ``github`` VCS is supported at this time.

        :param msg: Comment to post.
        :type msg: `str`
        :param pr: Pull request number on which to comment.
        :type pr: `str`,
        :param commit: Commit ID of the commit in the pull request necessitating comment.
        :type commit: `str`
        :param path: File path of the file necessitating comment.
        :type path: `str`
        :param max_retries: Number of times to attempt to post before failing the request. Wait time between retries is exponential.
        :returns: Dictionary containing VCS response.
        :rtype: `dict`
        """
        url                                     = self._pull(
            num                                 = pr,
            endpoint                            = constants.RepoProps.PULLS.value
        )
        body                                    = {
            "body"                              : msg,
            "commit_id"                         : commit,
            "path"                              : path,
            "subject_type"                      : "file"
            
        }
        return self._request(
            url                                 = url,
            body                                = body
        )

    def comment(self,
        msg                                     : str,
        pr                                      : str
    )                                           -> dict:
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
        url                                     = self._pull(
            num                                 = pr,
            endpoint                            = constants.RepoProps.COMMENTS.value
        )
        body                                    = {
            "body"                              : msg
        }
        return self._request(
            url                                 = url,
            body                                = body
        )