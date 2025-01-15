""" # objects.template
Object for managing Template loading and rendering.
"""
# Application Modules 
import conf 

# External Modules
from jinja2 import Environment, FileSystemLoader


class Template:
    inst = None
    """Singleton instance"""
    templates = None
    """Application templates"""
    dir = None
    """Directory containing templates"""
    ext = None
    """File extension of templates"""

    def __init__(
        self, 
        dir = conf.PERSIST["DIR"]["TEMPLATES"],
        ext = ".rst"
    ):
        """"
        Initialize *Templates* object.

        :param dir: Directory containg the templates. Defaults to ``data/templates``.
        :type dir: str
        :param ext: Extension of template files. Defaults to ``.rst``.
        :type ext: str
        """
        self.dir = dir
        self.ext = ext
        self.templates = Environment(
            loader=FileSystemLoader(self.dir)
        )

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        """
        Create single *Templates* object.
        """
        if not self.inst:
            self.inst = super(
                Template, 
                self
            ).__new__(self, *args, **kwargs)
        return self.inst

    def get(
        self, 
        template: str
    ):
        """
        Retrieve a named template. Named templates are given below,

        - summary: Template for directory summaries.
        - preamble: Template for chat preamble.
        - thread: Template for chat history.

        :param template: Name of the template to retrieve.
        :type template: str
        :returns: Jinja2 template
        """
        file_name = "".join([template, self.ext])
        return self.templates.get_template(file_name)

    def render(
        self, 
        template: str, 
        variables : dict
    ) -> str:
        """
        Render a template. 

        :param template: Template to render.
        :type template: str
        :param variables: Variables to inject into template.
        :type variables: dict
        :returns: A templated string.
        :rtype: str
        """
        return self.get(template).render(variables)