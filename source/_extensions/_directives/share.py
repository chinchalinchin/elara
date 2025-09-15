# allegany-galactic-nucleus/_ext/share.py

import os
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from urllib.parse import quote

class share_node(nodes.General, nodes.Element):
    pass

class ShareDirective(SphinxDirective):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'facebook': directives.flag,
        'twitter': directives.flag,
        'instagram': directives.flag,
    }

    def run(self):
        node = share_node('')
        node['facebook'] = 'facebook' in self.options
        node['twitter'] = 'twitter' in self.options
        node['instagram'] = 'instagram' in self.options
        return [node]

def process_share_nodes(app, doctree, fromdocname):
    if app.builder.format != 'html':
        return

    env = app.builder.env
    
    for node in doctree.traverse(share_node):
        base_url = app.config.html_baseurl or ''

        if base_url and not base_url.endswith('/'):
            base_url += '/'

        page_url = f"{base_url}{fromdocname}{app.builder.out_suffix}"
        
        title = env.titles.get(fromdocname, nodes.Text("")).astext()

        from_dir = os.path.dirname(fromdocname)
        facebook_icon_path = os.path.relpath('_static/svg/facebook.svg', from_dir).replace(os.path.sep, '/')
        twitter_icon_path = os.path.relpath('_static/svg/x.svg', from_dir).replace(os.path.sep, '/')
        instagram_icon_path = os.path.relpath('_static/svg/instagram.svg', from_dir).replace(os.path.sep, '/')
        
        html = app.builder.templates.render(
            'widgets/share.html', {
                'facebook': node['facebook'],
                'twitter': node['twitter'],
                'instagram': node['instagram'],
                'url': quote(page_url, safe=''),
                'title': quote(title, safe=''),
                'facebook_icon_path': facebook_icon_path,
                'twitter_icon_path': twitter_icon_path,
                'instagram_icon_path': instagram_icon_path,
                'app_id': app.config.facebook_app_id
            }
        )
        
        new_node = nodes.raw('', html, format='html')
        node.replace_self(new_node)

def setup(app):
    app.add_node(share_node)
    app.add_directive('share', ShareDirective)
    app.connect('doctree-resolved', process_share_nodes)
    app.add_config_value('facebook_app_id', '', 'html') 
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }