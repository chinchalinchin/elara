from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class map_node(nodes.General, nodes.Element):
    """A custom node for maps to be replaced later."""

    pass

class MapDirective(SphinxDirective):
    """
    Defines the .. map:: directive.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'latitude': directives.unchanged_required,
        'longitude': directives.unchanged_required,
        'width': directives.unchanged_required,
        'height': directives.unchanged_required
    }

    def run(self):
        node = map_node('')
        node['latitude'] = self.options['latitude']
        node['longitude'] = self.options['longitude']
        node['height'] = self.options['height']
        node['width'] = self.options['width']
        return [node]

def process_map_nodes(app, doctree, fromdocname):
    """
    This function is connected to the 'doctree-resolved' event.
    It finds all `map_node` instances in the document and replaces
    them with the final HTML for the Google Maps iframe.
    """

    if app.builder.format != 'html':
        return
    
    for node in doctree.traverse(map_node):
        map_html = app.builder.templates.render('widgets/map.html', {
            'map_latitude': node['latitude'],
            'map_longitude': node['longitude'],
            'maps_api_key': app.config.google_maps_api_key,
            'maps_width': node['width'],
            'maps_height': node['height']
        })
        
        new_node = nodes.raw('', map_html, format='html')
        node.replace_self(new_node)

def setup(app):
    """
    Register the directive and connect the event handler.
    """

    app.add_node(map_node)
    app.add_directive('map', MapDirective)
    app.add_config_value('google_maps_api_key', '', 'html')

    app.connect('doctree-resolved', process_map_nodes)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }