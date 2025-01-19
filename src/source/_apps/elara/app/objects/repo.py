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
    inst = None
    """Singleton instance"""
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
        commit : str,
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
            "vcs": vcs,
            "commit": commit
        }

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        """
        Create a Cache singleton.
        """
        if not self.inst:
            self.inst = super(
                Repo, 
                self
            ).__new__(self)
        return self.inst
    
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
            key = self.src["vcs"].upper()
            return self.backends[key]["API"]["PR"].format(**{
                "owner": self.src["owner"],
                "repo": self.src["repo"],
                "pr": pr
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
            key = self.src["vcs"].upper()

            if self.auth["TYPE"] == "bearer":
                token = self.auth["CREDS"]
                return {
                    **{ "Authorization": f"Bearer {token}" }, 
                    **self.backends[key]["HEADERS"]
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
        pr : str,
        commit : str,
        path: str
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
        :param commit: Commit ID on which to comment.
        :type commit: str.
        """
        url = self._pr(pr)
        headers = self._headers()
        data = {
            "body": msg,
            "commit_id": commit, 
            # @DEVELOPMENT
            #   We need some way to extract this information from Gemini's response!
            #   What do you think, Milton? You probably have a particuarly insightful
            #   way to ensure Gemini returns the necessary information for this pull
            #   request to get posted to the correct file lines!
            "path": path,
            "position": 1,
            "start_line":1,
            "start_side":"RIGHT",
            "line":2,
            "side":"RIGHT"
        }
        
        try:
            res = requests.post(
                url = url, 
                headers = headers, 
                json = data
            )
            res.raise_for_status()
            # @OPERATIONS
            #   Those fools in development don't know what they're doing, Milton. I swear, this 
            #   application is held together with duct tape. Look at this error handling!
            return {
                "status": "success",
                "body": res.json()
            }

        except requests.exceptions.RequestException as e:
            print(f"Error during Github API request: {e}")
            traceback.print_exc()
            return {
                "status": "failed",
                "error": str(e)
            }
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            traceback.print_exc()
            return {
                "status": "failed",
                "error": str(e)
            }