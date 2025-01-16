# Standard Library Modules
import os
# Application Modules
import conf
import parse
import model
import objects.repo as repo

def review(
    pr_number : str,
    branch : str ,
    model_type : str = conf.DEFAULTS["MODEL"],
    persona : str = conf.DEFAULTS["PERSONA"],
) -> str:
    """
    Placeholder for the code review logic.
    """
    source = repo.Repo()
    
    # 1. Get current working directory
    repo_dir = os.getcwd()  

    # 2. Call parse.summarize to get RST string of the repo
    summary = parse.summarize(repo_dir, stringify=True)
    # 1. Get current working directory
    # 2. Call parse.summarize to get RST string of git repo
    # 3. Call model.reply to send RST string to Gemini
    # 4. Take respond and add to pull request

    # NOTE: In step 4, we will probably need to use the Github API to post the comment to Github.
    #       Look up libraries we can use. I am hoping there is something simple we can install
    #       to accomplish this. If not, we will have to construct the POST request ourselves.
    return "placeholder"