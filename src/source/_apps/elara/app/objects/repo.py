""" 
objects.repo
------------

Object for external Version Control System. 
"""
# Standard Library Modules 
import logging 
import traceback

# External Modules
import requests

logger = logging.getLogger(__name__)

class Repo:
    auth = None
    """Authentication configuration for VCS backend"""
    src = None
    """VCS source information"""
    backends = None
    """Backend configurations"""

    def __init__(
        self,
        repository : str, 
        owner : str,
        vcs : str ,
        auth : str,
        backends : dict
    ):
        """
        Initialize Repository object.

        :param repo: Name of the VCS repository.
        :type repo: str
        :param owner: Username of the owner of the repository.
        :type owner: str
        :param vcs: Type of VCS backend to use. Currently supports: `github`. Defaults to the value of the ``VCS`` environment variable.
        :type vcs: str
        :param auth: Authentication configuration for the VCS backend. Currently supposed token-based authorization headers. Defaults to the token value in the ``VCS_TOKEN`` environment variable.
        :type auth: dict
        :param backends: Dictionary containing backend configurations.
        :type backends: dict

        .. note::

            `auth` must be formatted as follows,

            {
                "VCS": "<github | bitbucket | codecommit>",
                "AUTH": {
                    "TYPE": "<bearer | oauth | etc. >",
                    "CREDS": "will change based on type."
                }
            }
        
        .. note::

            Only ``github`` VCS is supported at this time.
            
        """
        self.auth = auth
        self.backends = backends
        self.src = {
            "owner": owner,
            "repo": repository,
            "vcs": vcs
        }

    
    def __iter__(self):
        for k, v in self.src.items(): 
            yield (k, v)

    def _pr(
        self, 
        pr
    ) -> str | None:
        """
        Returns the POST URL for the VCS REST API.

        .. note::

            Only ``github`` VCS is supported at this time.
            
        :param pr: Pull request number for the POST.
        :type pr: str
        :returns: POST URL
        :rtype: str
        """
        if self.src["vcs"] == "github":
            return self.backends["GITHUB"]["API"]["PR"]["ISSUE"].format(**{
                **{ "pr": pr }, 
                **self.src
            })
        
        raise ValueError(f"Unsupported VCS: {self.src['vcs']}")
    
    def _headers(self):
        """
        Returns the necessary headers for a request to the VCS backend. 

        .. note::

            Only ``github`` VCS is supported at this time.
            
        :returns: Dictionary of headers
        :rtype:  dict
        """
        if self.src["vcs"] == "github":
            if self.auth["TYPE"] == "bearer":
                token = self.auth["CREDS"]
                return {
                    **{ "Authorization": f"Bearer {token}" }, 
                    **self.backends["GITHUB"]["HEADERS"]
                }
            
        raise ValueError(f"Unsupported auth type: {self.auth['TYPE']} or VCS: {self.src['vcs']}")

    def vars(self):
        """
        Retrieve VCS metadata, formatted for templating.
        """
        return { "repository": self.src }
    
    def comment(
        self,
        msg : str,
        pr : str
    ):
        """
        Post a comment to a pull request on the VCS backend. Links below detail the specific VCS provider endpoints,

        - **Github**: `Github REST API Docs <https://docs.github.com/en/rest/pulls/comments?apiVersion=2022-11-28#create-a-review-comment-for-a-pull-request>

        .. note::

            Only ``github`` VCS is supported at this time.

        :param msg: Comment to post.
        :type msg: str
        :param pr: Pull request number on which to comment.
        :type pr: str
        """
        try:
            logger.debug(f"Making HTTP call to {self._pr(pr)}")

            res = requests.post(
                url = self._pr(pr), 
                headers = self._headers(), 
                json = { "body": f"MILTON SAYS: \n\n {msg}" }
            )

            logger.debug(res)

            res.raise_for_status()
            
            return {
                "status": "success",
                "body": res.json()
            }

        except requests.exceptions.RequestException as e:
            logger.error(f"Error during Github API request: {e}")
            traceback.print_exc()
            return {
                "status": "failed",
                "error": str(e)
            }
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()
            return {
                "status": "failed",
                "error": str(e)
            }