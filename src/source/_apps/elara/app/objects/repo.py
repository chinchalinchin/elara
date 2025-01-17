""" objects.repo
Object for external Version Control System. 
"""
# Standard Library Modules 
import logging 

# Application Modules
import traceback
import conf 

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

    def __init__(
        self,
        repo : str, 
        owner : str,
        commit : str,
        vcs : str= conf.REPOS["VCS"],
        auth : str= conf.REPOS["AUTH"]
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
        self.src = {
            "owner": owner,
            "repo": repo,
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
            return conf.REPOS["BACKENDS"]["GITHUB"]["API"]["PR"].format(**{
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
            if self.auth["TYPE"] == "bearer":
                token = self.auth["CREDS"]
                return {
                    **{ "Authorization": f"Bearer {token}" }, 
                    **conf.REPOS["BACKENDS"]["GITHUB"]["HEADERS"]
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
            "path": path
            
        }
        
        # @OPERATIONS
        #   THIS IS WHERE THE 422 ARE HAPPENING! HELP US! OH GOD! THE HUMANITY!
        # @OPERATIONS
        try:
            res = requests.post(
                url = url, 
                headers = headers, 
                json = data
            )
            res.raise_for_status()
            # @OPERATIONS
            #   WHAT IS GOING!? THE PRODUCTION SYSTEMS ARE BREAKING HERE! THE LOGS ARE SHOWING:
            # 
            #   EXAMPLE LOG:
            #   
            #           Error during Github API request: 422 Client Error: Unprocessable Entity for url: https://api.github.com/repos/chinchalinchin/elara/pulls/1/comments
            #           Traceback (most recent call last):
            #           File "/home/grant/Projects/elara/src/source/_apps/elara/app/objects/repo.py", line 179, in comment
            #               res.raise_for_status()
            #           File "/home/grant/Projects/elara/venv/lib/python3.12/site-packages/requests/models.py", line 1024, in raise_for_status
            #               raise HTTPError(http_error_msg, response=self)
            #           requests.exceptions.HTTPError: 422 Client Error: Unprocessable Entity for url: https://api.github.com/repos/chinchalinchin/elara/pulls/1/comments
            #           {'status': 'failed', 'error': '422 Client Error: Unprocessable Entity for url: https://api.github.com/repos/chinchalinchin/elara/pulls/1/comments'}
            #
            #   WE ARE GETTING 422 RESPONSE CODES BY THE HUNDREDS, MILTON! ACCORDING TO THE GITHUB DOCS, THIS MEANS:
            #
            #       Validation failed, or the endpoint has been spammed.
            #
            #   WHAT DO WE, MILTON!? WHAT ERRORS SHOULD WE BE CATCHING!? WHAT INFORMATION
            #   DO YOU NEED TO DEBUG THIS? OH GOD! THE SERVERS ARE OVERHEATING!
            # @OPERATIONS
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