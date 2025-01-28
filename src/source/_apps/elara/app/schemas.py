"""
app.py
------

Objects for managing application and service responses.
"""
# Standard Library Modules
import dataclasses

@dataclasses.dataclass
class Output:
    """
    Data structure for managing application output.
    """
    prompt                  : str | None = None
    response                : dict | None = None
    includes                : dict | None = None

    def to_dict(self):
        return {
            field.name: getattr(self, field.name)
            for field in dataclasses.fields(self)
            if getattr(self, field.name) is not None
        }


@dataclasses.dataclass
class Arguments:
    """
    Data astructure for managing application arguments.
    """
    # ARGUMENT ROOT
    operation               : str | None = None
    # MAIN ARGUMENTS
    prompt                  : str | None = None
    """Prompt to post to model"""
    current_model           : str | None = None
    """Version of the model"""
    current_persona         : str | None = None
    """Persona of the model"""
    current_prompter        : str | None = None
    """Identity of the prompter"""
    # PATH ARGUMENTS
    directory               : str | None = None 
    """Local directory to inject into prompt"""
    output                  : str | None = None
    """Local directory to write model response"""
    # FLAG ARGUMENTS
    render                  : bool = False
    """Launch an interactive terminal"""
    terminal                : bool = False 
    """Flag to render contextualized prompt without posting."""
    view                    : bool = False
    """Flag to print output"""
    # VCS ARGUMENTS
    pull                    : str | None = None
    """Pull request number for reviewing"""
    repository              : str | None = None 
    """Name of the remote VCS repository hosting local directory."""
    owner                   : str | None = None 
    """Username of the remote VCS repository owner."""
    # ORCHESTRATION ARGUMENTS
    concepts                : list = dataclasses.field(default_factory=list)
    """List of concept words to use for brainstorming"""
    #  META ARGUMENTS
    clear                   : list = dataclasses.field(default_factory=list)
    """List of personas whose data is to be cleared."""
    pairs                   : list = dataclasses.field(default_factory=list)
    """List of 'key=value' strings to save to cache."""


    def has_vcs_args(self):
        return self.repository is not None and self.owner is not None


    def has_dir_args(self):
        return self.directory is not None
    

    def has_tty_args(self):
        return self.terminal is not None
    
    
    def to_dict(self):
        return {
            field.name: getattr(self, field.name)
            for field in dataclasses.fields(self)
            if getattr(self, field.name) is not None
        }


@dataclasses.dataclass
class FileReview:
    path                    : str
    comments                : str
    bugs                    : str | None = None
    amendments              : str | None = None


@dataclasses.dataclass
class ReviewResponse:
    score                   : str = None
    overall                 : str = None
    files                   : list[FileReview] = dataclasses.field(default_factory=list)
