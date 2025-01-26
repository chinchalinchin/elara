""" 
objects.template.py
===================

Object for managing template loading and rendering.

template.Template
-----------------

Templates are organized through the hierarchy of application's functions.

**Functional Templates**: Templates that encapsulate a function.

    - analyze
    - brainstorm
    - converse
    - request
    - review
    - output

These functional templates are built out of modular templates. Modular templates are broken into several categories.

**Context Templates**: These templates serve as plugins for the model context.
        
    - _context/external
    - _context/identities
    - _context/internal
    - _context/language

**Interface Templates**: These templates give Gemini information regarding the interface that is being used to send prompts.

    - _interfaces/cli

**Report Templates**: These templates are used to render application reports

    - _reports/models
    - _reports/service
    - _reports/summary

**Response Templates**: These templates are used to render Gemini's structured output.

    - _responses/analyze
    - _responses/brainstorm
    - _responses/converse
    - _responses/request
    - _responses/review

**Schema Templates**: These templates are used to provide Gemini information about the schema imposed on the model's structured output.

    - _schemas/analyze
    - _schemas/brainstorm
    - _schemas/converse
    - _schemas/request
    - _schemas/review

"""
# External Modules
import jinja2


class Template:
    """
    Class for managing application templates. 
    """
    templates = None
    """Application templates"""
    directory = None
    """Directory containing templates"""
    extension = None
    """File extension of templates"""

    def __init__(self, 
        directory : str,
        extension : str
    ) -> None:
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


    def get(self, 
        template: str
    ) -> jinja2.Template:
        """
        Retrieve a template. 

        :param template: Name of the template to retrieve.
        :type template: str
        :returns: Jinja2 template
        """
        file_name = "".join([template, self.extension])
        return self.templates.get_template(file_name)


    def render(self, 
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