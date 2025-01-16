""" objects.repo
Object for external Version Control System. 
"""

import conf 

class Repo:
    inst = None
    """Singleton instance"""
    vcs = None
    """Version control backend"""
    auth = None
    """Authentication configuration for VCS backend"""

    def __init__(
        self, 
        vcs = conf.REVIEW["VCS"],
        auth = conf.REVIEW["AUTH"]
    ):
        """
        Initialize Repo

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
            
    def _pr(
        self, 
        repo, 
        owner,
        pr
    ) -> str | None:
        if self.vcs == "github":
            return f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr}/comments"
        return None
    
    def urls(
        self, 
        repo : str, 
        pr : str
    ) -> str | None:
        if self.vcs == "github":
            return {
                "pr": self._pr(repo, pr)
            }
        return None
    
    def headers(self):
        if self.vcs == "github":
            if self.auth["TYPE"] == "bearer":
                token = self.auth["CREDS"]
                return {
                    **{ "Authorization": f"Bearer {token}" }, 
                    **conf.REVIEW["BACKENDS"]["GITHUB"]["HEADERS"]
                }

    def comment(self):
        pass 

### From Github REST API docs: https://docs.github.com/en/rest/pulls/comments?apiVersion=2022-11-28#create-a-review-comment-for-a-pull-request

## Example
# curl -L \
#   -X POST \
#   -H "Accept: application/vnd.github+json" \
#   -H "Authorization: Bearer <YOUR-TOKEN>" \
#   -H "X-GitHub-Api-Version: 2022-11-28" \
#   https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/comments \
#   -d '{"body":"Great stuff!","commit_id":"6dcb09b5b57875f334f61aebed695e2e4193db5e","path":"file1.txt","start_line":1,"start_side":"RIGHT","line":2,"side":"RIGHT"}'


## Path parameters
# Name, Type, Description
# owner string Required
# The account owner of the repository. The name is not case sensitive.

# repo string Required
# The name of the repository without the .git extension. The name is not case sensitive.

# pull_number integer Required
# The number that identifies the pull request.

## Body parameters
# Name, Type, Description
# body string Required
# The text of the review comment.

# commit_id string Required
# The SHA of the commit needing a comment. Not using the latest commit SHA may render your comment outdated if a subsequent commit modifies the line you specify as the position.

# path string Required
# The relative path to the file that necessitates a comment.

# position integer
# This parameter is closing down. Use line instead. The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.

# side string
# In a split diff view, the side of the diff that the pull request's changes appear on. Can be LEFT or RIGHT. Use LEFT for deletions that appear in red. Use RIGHT for additions that appear in green or unchanged lines that appear in white and are shown for context. For a multi-line comment, side represents whether the last line of the comment range is a deletion or addition. For more information, see "Diff view options" in the GitHub Help documentation. Can be one of: LEFT, RIGHT

# line integer
# Required unless using subject_type:file. The line of the blob in the pull request diff that the comment applies to. For a multi-line comment, the last line of the range that your comment applies to.

# start_line integer
# Required when using multi-line comments unless using in_reply_to. The start_line is the first line in the pull request diff that your multi-line comment applies to. To learn more about multi-line comments, see "Commenting on a pull request" in the GitHub Help documentation.

# start_side string
# Required when using multi-line comments unless using in_reply_to. The start_side is the starting side of the diff that the comment applies to. Can be LEFT or RIGHT. To learn more about multi-line comments, see "Commenting on a pull request" in the GitHub Help documentation. See side in this table for additional context. Can be one of: LEFT, RIGHT, side

# in_reply_to integer
# The ID of the review comment to reply to. To find the ID of a review comment with "List review comments on a pull request". When specified, all parameters other than body in the request body are ignored.

# subject_type string
# The level at which the comment is targeted. Can be one of: line, file


# HTTP response status codes 
# Status code	Description
# 201 Created

# 403 Forbidden

# 422 Validation failed, or the endpoint has been spammed.