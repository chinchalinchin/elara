""" 
objects.template.py
===================

Object for managing template loading and rendering.

template.Template
-----------------

Templates are organized through the hierarchy of application's functions. All application templates can be found in the ``data/templates`` directory. The templates on the first level of this directoy correspond to core application functions. The templates in the subdirectories corresponds to modular templates.

**Functional Templates**
    Templates that encapsulate a function.

- analyze
- brainstorm
- converse
- request
- review
- output

These functional templates are built out of modular templates. Modular templates are broken into several categories.

TODO: document /data/templates structure here

"""
# Standard Library Modules
import logging 
import json

# External Modules
import jinja2


logger                      = logging.getLogger(__name__)


class Template:
    """
    Class for managing application templates. 
    """
    templates               = None
    """Application templates"""
    directory               = None
    """Directory containing templates"""
    extension               = None
    """File extension of templates"""

    def __init__(self,  directory: str, extension: str) -> None:
        """"
        Initialize a Template object.

        :param directory: Directory containg the templates. Defaults to ``data/templates``.
        :type directory: str
        :param extension: Extension of template files. Defaults to ``.rst``.
        :type extension: str
        """
        self.directory      = directory
        self.extension      = extension
        self.templates      = jinja2.Environment(
            loader          = jinja2.FileSystemLoader(self.directory)
        )
        self.templates.filters.update({
            "prettify"      : self._prettify,
            "indent"        : self._indent
        })


    @staticmethod
    def _prettify(value, indent: int = 4):
        """
        Jinja2 filter to pretty-print JSON.

        :param value: The JSON string to format
        :type value: `str`
        :param indent: The number of spaces to use for indentation. Defaults to 4.
        :type indent: `str`
        :returns: A pretty-printed JSON string, or the original value if it's not a valid JSON string.
        :rtype: `str
        """
        try:
            parsed_json     = json.loads(value)
            return json.dumps(parsed_json, indent=indent, sort_keys=True)
        except (ValueError, TypeError) as e:
            logger.error(e)
            return value
        

    @staticmethod
    def _indent(value) -> str:
        """
        Jinja2 filter to indent new lines in a string.

        :param value: String to be indented.
        :type value: `str`
        :returns: Indented string
        :rtype: `str`
        """
        return value.replace('\n', '\n    ')

    def get(self, template: str, ext: str | None = None) -> jinja2.Template:
        """
        Retrieve a template. 

        :param template: Name of the template to retrieve.
        :type template: `str`
        :param ext: Extension of the template. Defaults to ``.rst``.
        :type ext: `str`
        :returns: A template
        :rtype: `jinja2.Template`
        """
        extension           = self.extension if ext is None else ext
        file_name           = "".join([template, extension])
        return self.templates.get_template(file_name)


    def render(self, variables: dict, template: str = "application", extension: str | None = None) -> str:
        """
        Render a template. 

        :param temp: Template to render.
        :type temp: `str`
        :param variables: Variables to inject into template.
        :type variables: `dict`
        :param ext: Extension of the template. Defaults to ``.rst``.
        :type ext: `str`
        :returns: A templated string.
        :rtype: `str`
        """
        return self.get(template, extension).render(variables)
    

    def service(self, template: str, service: str, variables: dict, extension: str = ".md") -> str:
        """
        Render a VCS template. 

        :param template: Template to render.
        :type template: `str`
        :param variables: Variables to inject into template.
        :type variables: `dict`
        :param service: Type of service.
        :type service: `str`
        :param ext: Extension of the template. Defaults to ``.rst``.
        :type ext: `str`
        :returns: A templated string.
        :rtype: `str`
        """
        temp                = "_functions/_services/_{service}/{template}".format(
            template        = template,
            service         = service
        )
        return self.render(variables, temp, extension)