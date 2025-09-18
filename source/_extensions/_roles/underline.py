
from docutils import nodes, utils

def underline(name: str, rawtext: str, text: str, lineno: int,
               inliner, options={}, content=[]):
    node = nodes.inline(rawtext, utils.unescape(text), classes=['underline'])
    return [node], []

def setup(app):
    app.add_role('underline', underline)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }