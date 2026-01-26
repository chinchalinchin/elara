
from docutils import nodes, utils

def redacted(name: str, rawtext: str, text: str, lineno: int,
               inliner, options={}, content=[]):
    node = nodes.inline(rawtext, utils.unescape(text), classes=['redacted'])
    return [node], []

def handwritten(name: str, rawtext: str, text: str, lineno: int,
               inliner, options={}, content=[]):
    node = nodes.inline(rawtext, utils.unescape(text), classes=['handwritten'])
    return [node], []

def small(name: str, rawtext: str, text: str, lineno: int,
               inliner, options={}, content=[]):
    node = nodes.inline(rawtext, utils.unescape(text), classes=['small'])
    return [node], []

def strike(name: str, rawtext: str, text: str, lineno: int,
               inliner, options={}, content=[]):
    node = nodes.inline(rawtext, utils.unescape(text), classes=['strike'])
    return [node], []

def tiny(name: str, rawtext: str, text: str, lineno: int,
               inliner, options={}, content=[]):
    node = nodes.inline(rawtext, utils.unescape(text), classes=['tiny'])
    return [node], []

def underline(name: str, rawtext: str, text: str, lineno: int,
               inliner, options={}, content=[]):
    node = nodes.inline(rawtext, utils.unescape(text), classes=['underline'])
    return [node], []

def setup(app):
    app.add_role('redacted', redacted)
    app.add_role('handwritten', handwritten)
    app.add_role('small', small)
    app.add_role('strike', strike)
    app.add_role('tiny', tiny)
    app.add_role('underline', underline)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }