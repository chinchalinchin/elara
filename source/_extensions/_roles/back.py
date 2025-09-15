import os
from docutils import nodes
from sphinx.util.docutils import SphinxRole

class back_node(nodes.General, nodes.Element):
    pass

class BackRole(SphinxRole):
    def run(self):
        # The argument of the role is the reference label
        ref = self.text
        node = back_node('')
        node['ref'] = ref
        return [node], []

def process_back_nodes(app, doctree, fromdocname):
    if app.builder.format != 'html':
        return

    std_domain = app.env.get_domain('std')

    for node in doctree.traverse(back_node):
        ref = node['ref']
        target_docname = None
        target_anchor = ''

        # First, try to resolve the ref as a standard Sphinx label
        if ref in std_domain.labels:
            target_docname, target_anchor, _ = std_domain.labels[ref]
        # As a fallback, check if the ref is a valid docname
        elif app.env.docname_exists(ref):
            target_docname = ref
        else:
            app.logger.warning(f'back role reference not found: {ref}', location=node)
            node.replace_self([])
            continue

        # Build the URL, including the anchor if it exists
        link_url = app.builder.get_relative_uri(fromdocname, target_docname)
        if target_anchor:
            link_url += '#' + target_anchor

        # Correctly calculate the relative path for the SVG icon
        from_dir = os.path.dirname(fromdocname)
        icon_path_from_src = '_static/svg/back.svg'
        icon_path = os.path.relpath(icon_path_from_src, from_dir).replace(os.path.sep, '/')
        
        # Render the template
        html = app.builder.templates.render('widgets/back.html', {
            'link_url': link_url,
            'icon_path': icon_path,
        })
        
        new_node = nodes.raw('', html, format='html')
        node.replace_self(new_node)


def setup(app):
    app.add_node(back_node)
    app.add_role('back', BackRole())
    app.connect('doctree-resolved', process_back_nodes)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }