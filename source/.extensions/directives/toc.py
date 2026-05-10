import os
from docutils import nodes
from sphinx.directives.other import TocTree
from sphinx import addnodes

class CustomTocTreeDirective(TocTree):
    """Overrides the default toctree directive to enforce a custom view."""
    
    def run(self):
        # Constraint: Always default to a depth of 1
        if 'maxdepth' not in self.options:
            self.options['maxdepth'] = 1
            
        result = super().run()
        
        # Constraint: The number of dots should be calculated by the directive.
        # We calculate an excess baseline string here; the CSS will handle scaling and clipping.
        calculated_dots = "." * 300
        
        for node in result:
            if isinstance(node, nodes.compound):
                for child in node.children:
                    if isinstance(child, addnodes.toctree):
                        child['calculated_dots'] = calculated_dots
                        
        return result

def process_custom_toctree(app, doctree, fromdocname):
    """Intercepts and translates resolved toctrees into the Jinja2 template."""
    if app.builder.format != 'html':
        return
        
    for node in doctree.traverse(addnodes.toctree):
        # Resolve the toctree to extract the valid internal links and titles
        resolved_toc = app.env.resolve_toctree(fromdocname, app.builder, node, prune=True, maxdepth=1)
        
        if resolved_toc is None:
            continue
            
        toc_items = []
        page_num = 1
        dots = node.get('calculated_dots', '.' * 300)
        
        for ref_node in resolved_toc.traverse(nodes.reference):
            if ref_node.get('internal', True):
                toc_items.append({
                    'title': ref_node.astext(),
                    'url': ref_node['refuri'],
                    'page_num': page_num,
                    'dots': dots
                })
                page_num += 1
                
        html = app.builder.templates.render('toc.html', {
            'caption': node.get('caption', 'Contents'),
            'items': toc_items
        })
        
        new_node = nodes.raw('', html, format='html')
        node.replace_self(new_node)

def setup(app):
    # Register the override to intercept default `toctree` calls
    app.add_directive('toctree', CustomTocTreeDirective, override=True)
    app.connect('doctree-resolved', process_custom_toctree)
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }