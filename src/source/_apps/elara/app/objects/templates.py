""" # objects.template
Object for managing Template loading and rendering.
"""
# Application Modules 
import conf 

# External Modules
from jinja2 import Environment, FileSystemLoader


class Template:
    instance = None
    templates = None
    template_dir = None
    template_ext = None

    def __init__(
        self, 
        template_dir = conf.PERSIST["DIR"]["TEMPLATES"],
        template_ext = ".rst"
    ):
        self.template_dir = template_dir
        self.template_ext = template_ext
        self._load()

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        if not self.instance:
            self.instance = super(
                Template, 
                self
            ).__new__(self, *args, **kwargs)
        return self.instance
    
    def _load(
        self, 
    ):
        """Load Templates"""
        self.templates = Environment(
            loader=FileSystemLoader(self.template_dir)
        )


    def get(self, template):
        file_name = ".".join([template, self.template_ext])
        return self.templates.get(file_name)

    def render(self, template, vars):
        temp = self.get(template)
        return temp.render(vars)