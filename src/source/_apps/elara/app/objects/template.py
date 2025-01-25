""" 
objects.template
----------------

Object for managing template loading and rendering.
"""
# External Modules
import jinja2


class Template:
    templates = None
    """Application templates"""
    directory = None
    """Directory containing templates"""
    extension = None
    """File extension of templates"""

    def __init__(
        self, 
        directory : str,
        extension : str
    ):
        """"
        Initialize *Templates* object.

        :param directory: Directory containg the templates. Defaults to ``data/templates``.
        :type directory: str
        :param extension: Extension of template files. Defaults to ``.rst``.
        :type extension: str
        """
        self.directory = directory
        self.extension = extension
        self.templates = jinja2.Environment(
            loader = jinja2.FileSystemLoader(self.directory)
        )


    def get(
        self, 
        template: str
    ):
        """
        Retrieve a named template. Named templates are given below,

        - review: Template for pull request reviews.
        - summary: Template for directory summaries.
        - preamble: Template for chat preamble.
        - thread: Template for chat history.

        :param template: Name of the template to retrieve.
        :type template: str
        :returns: Jinja2 template
        """
        file_name = "".join([template, self.extension])
        return self.templates.get_template(file_name)


    def render(
        self, 
        temp: str, 
        variables : dict
    ) -> str:
        """
        Render a template. 

        :param temp: Template to render.
        :type temp: str
        :param variables: Variables to inject into template.
        :type variables: dict
        :returns: A templated string.
        :rtype: str
        """
        return self.get(temp).render(variables)