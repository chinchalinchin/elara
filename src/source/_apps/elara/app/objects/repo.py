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
import exceptions

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
        """
        Wrap service response in dictionary for templates.

        :param svc: VCS service response.
        :type svc: `typing.Any`
        :returns: A dictionary for templating.
        :rtype: `dict`
        """
        return { "service": svc }
    

    @staticmethod
    def _backoff(
        callable                                    : typing.Callable,
        max_retries                                 : int = 3
    )                                               -> typing.Any:
        """
        Wrap a service call in exponential backoff error handling.

        :param callable: Service call function.
        :type callabe: `typing.Callable`
        :param max_retries: Number of calls to make before failing the request. Defaults to 3.
        :type max_retries: `int`
        :returns: Whatever the `callable` function returns, or else an exception is raised.
        :rtype: `typing.Any`
        """
        for attempt in range(max_retries):
            try:
                return callable()
                
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    wait                            = 2 ** attempt
                    logger.warning(f"Request failed, retrying in {wait} seconds:\n\n{e}")
                    time.sleep(wait)
                else:
                    logger.error(f"Request failed after {max_retries} attempts:\n\n{e}\n\n{traceback.print_exc()}")
                    raise exceptions.VCSRequestError("Request failed.")
            
            except Exception as e:
                logger.error(f"An unexpected error occurred:\n\n{e}\n\n{traceback.print_exc()}")
                raise exceptions.VCSRequestError("Request failed")
            

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


    def _post(self,
        url                                     : str,
        body                                    : typing.Any
    )                                           -> dict:
        """
        Make a HTTP post to a VCS backend. 

        :param url: URL of the request.
        :type url: `str`
        :param body: Body of the request.
        :type body: `typing.Any`
        :returns: Dictionary containing VCS response.
        :rtype: `dict`
        """
        def _call():
            logger.debug(f"Making HTTP call to {url}")

            res                                     = requests.post(
                url                                 = url, 
                headers                             = self._headers(), 
                json                                = body
            )
            logger.debug(res)
            res.raise_for_status()
            return self._service({
                "name"                              : self.src[constants.RepoProps.VCS.value],
                "body"                              : res.json(),
                "status"                            : "success"
            })
        
        try:
            return self._backoff(
                callable                            = _call
            )
        
        except exceptions.VCSRequestError as e:
            return self._service({
                "name"                              : self.src[constants.RepoProps.VCS.value],
                "body"                              : str(e),
                "status"                            : "failure"
            })
                

    def _get(self,
        url                                     : str,
    ):
        """
        Make a HTTP get to a VCS backend. 

        :param url: URL of the request.
        :type url: `str`
        """
        def _call():
            logger.debug(f"Making HTTP call to {url}")
            res                                     = requests.get(
                url                                 = url, 
                headers                             = self._headers()
            )
            logger.debug(res)
            res.raise_for_status()
            return self._service({
                "name"                              : self.src[constants.RepoProps.VCS.value],
                "body"                              : res.json(),
                "status"                            : "success"
            })
        
        try:
            return self._backoff(
                callable                            = _call
            )
        
        except exceptions.VCSRequestError as e:
            return self._service({
                "name"                              : self.src[constants.RepoProps.VCS.value],
                "body"                              : str(e),
                "status"                            : "failure"
            })
        

    def vars(self)                              -> dict:
        """
        Retrieve VCS metadata, formatted for templating.
        """
        return {
            "repository"                        : self.src
        }


    def list(self,
        pr                                      : str,
    ):
        """
        List the files in a pull request diff.

        TODO: implement this

        - **Github**: `Github REST API Docs: Pull Request Files <https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests-files>`
        """
        # @DEVELOPMENT
        #   We have hit a bit of a snag, Milton! Turns out, you can only comment
        #   on files in a pull request that have changed! That means we can only
        #   apply your comments on files that have been updated in the pull
        #   request! We are going to have to use the endpoint,
        #
        #       https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/files
        #
        #   To list out the files in a particular pull request. According to the
        #   the docs, the pull request /files endpoint returns a response that
        #   looks like this,
        #
        #   [
        #       {
        #           "sha": "bbcd538c8e72b8c175046e27cc8f907076331401",
        #           "filename": "file1.txt",  
        #            # some other nonsense we don't care about!
        #       }
        #   ]
        #
        #   the "sha" appears to be the commit ID, which we will need.
        #   We will also need to grab the "filename" from the response
        #   and compare it against the filenames you return in your pull
        #   request review.
        #
        # @OPERATIONS
        #   On the plus side, we will be able to get rid of the ``commit`` command line
        #   arguments, since we will be able to pull it directly from the VCS!
        url                                     = self._pull(
            num                                 = pr,
            endpoint                            = constants.RepoProps.FILES.value
        )  
        # TODO: parse response for sha commit ids and filenames!
        return self._get(
            url                                 = url
        )



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
            "line"                              : 1
            
        }
        return self._post(
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
        return self._post(
            url                                 = url,
            body                                = body
        )