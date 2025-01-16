""" objects.repo
Object for external Version Control System. 
"""

# Application Modules
import conf 

# External Modules
import requests

class Repo:
    inst = None
    """Singleton instance"""
    vcs = None
    """Version control backend"""
    auth = None
    """Authentication configuration for VCS backend"""
    repo = None
    """Name of the VCS repository"""
    owner = None
    """Username of the repository owner."""

    def __init__(
        self,
        repo : str, 
        owner : str,
        vcs : str= conf.REVIEW["VCS"],
        auth : str= conf.REVIEW["AUTH"]
    ):
        """
        Initialize Repo

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
        """
        self.vcs = vcs
        self.auth = auth
        self.repo = repo
        self.owner = owner

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
            ).__new__(self, *args, **kwargs)
        return self.inst

    def __dir__(self):
        return {
            "repo": self.repo,
            "vcs": self.vcs,
            "owner": self.owner
        }
      
    def _pr(
        self, 
        pr
    ) -> str | None:
        """
        Returns the POST URL for the VCS REST API.

        :param pr: Pull request number for the POST.
        :type pr: str
        :returns: POST URL
        :rtype: str
        """
        if self.vcs == "github":
            return f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{pr}/comments"
        return None
    
    def _headers(self):
        """
        Returns the necessary headers for a request to the VCS backend. 

        :returns: Dictionary of headers
        :rtype:  dict
        """
        if self.vcs == "github":
            if self.auth["TYPE"] == "bearer":
                token = self.auth["CREDS"]
                return {
                    **{ "Authorization": f"Bearer {token}" }, 
                    **conf.REVIEW["BACKENDS"]["GITHUB"]["HEADERS"]
                }

    def comment(
        self,
        msg : str,
        pr : str,
        commit : str
    ):
        """
        Post a comment to a pull request on the VCS backend. Links detail the specific VCS provider endpoints,

        - **Github**: `Github REST API Docs <https://docs.github.com/en/rest/pulls/comments?apiVersion=2022-11-28#create-a-review-comment-for-a-pull-request>

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
            # According to Github REST api, `path` should be:
            #
            #       The relative path to the file that necessitates a comment.
            #
            # TODO: need to figure out how to get Gemini to output
            #       filepath!
            "path": "TODO" 
            
        }
        return requests.post(
            url = url, 
            headers = headers, 
            json = data
        )