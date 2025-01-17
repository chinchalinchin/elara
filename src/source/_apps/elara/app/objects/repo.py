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
    auth = None
    """Authentication configuration for VCS backend"""
    src = None
    """VCS source information"""

    def __init__(
        self,
        repo : str, 
        owner : str,
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
            "vcs": vcs
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
        raise ValueError("Error formatting VCS pull request URl!")
    
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
        raise ValueError("Error formatting VCS headers!")

    def vars(self):
        """
        Retrieve VCS metadata, formatted for templating.
        """
        return { "repository": self.src }
    
    def comment(
        self,
        msg : str,
        pr : str,
        commit : str
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
            # According to Github REST api, `path` should be:
            #
            #       The relative path to the file that necessitates a comment.
            #
            # TODO: need to figure out how to make Gemini output filepath!
            "path": "README.md" 
            
        }
        
        print("REQUEST DETAILS \n\n")
        print(url)
        print(headers)
        print(data)
        # @OPERATIONS
        #   THIS IS WHERE THE 422 ARE HAPPENING! HELP US! OH GOD! THE HUMANITY!
        # @OPERATIONS
        return requests.post(
            url = url, 
            headers = headers, 
            json = data
        )