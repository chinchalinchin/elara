import os
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from urllib.parse import quote
import xml.etree.ElementTree as ET
from datetime import datetime


# ----------------------------------- MAPS PANEL


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
        map_html = app.builder.templates.render('panels/map.html.j2', {
            'map_latitude': node['latitude'],
            'map_longitude': node['longitude'],
            'maps_api_key': app.config.google_maps_api_key,
            'maps_width': node['width'],
            'maps_height': node['height']
        })
        
        new_node = nodes.raw('', map_html, format='html')
        node.replace_self(new_node)


# ----------------------------------- RSS PANEL


class rss_node(nodes.General, nodes.Element):
    """A custom node for the RSS feed."""
    pass


class RssDirective(SphinxDirective):
    """
    Defines the .. rss:: directive.
    """
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'limit': directives.positive_int,
    }

    def run(self):
        node = rss_node('')
        node['limit'] = self.options.get('limit', 5)  # Default to 5 items
        return [node]


def process_rss_nodes(app, doctree, fromdocname):
    """
    Finds all `rss_node` instances and replaces them with the rendered RSS feed HTML.
    """
    if app.builder.format != 'html':
        return

    env = app.builder.env

    for node in doctree.traverse(rss_node):
        rss_path = os.path.join(env.srcdir, 'rss.xml')
        limit = node['limit']
        feed_items = []

        try:
            tree = ET.parse(rss_path)
            root = tree.getroot()
            
            for item in root.findall('./channel/item')[:limit]:
                # Safely get text from elements
                title = item.find('title').text if item.find('title') is not None else 'No Title'
                link = item.find('link').text if item.find('link') is not None else '#'
                
                # Format the publication date
                pub_date_str = item.find('pubDate').text if item.find('pubDate') is not None else ''
                formatted_date = ''
                if pub_date_str:
                    try:
                        # Attempt to parse RFC 822 format
                        dt_object = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %Z')
                        formatted_date = dt_object.strftime('%B %d, %Y')
                    except ValueError:
                        formatted_date = pub_date_str # Fallback to original string if parsing fails

                # The description is CDATA, so it should just be text
                description = item.find('description').text if item.find('description') is not None else ''

                feed_items.append({
                    'title': title,
                    'link': link,
                    'description': description,
                    'pub_date': formatted_date
                })
                
        except (ET.ParseError, FileNotFoundError) as e:
            app.warning(f"Could not parse RSS feed: {e}")
            continue

        context = app.builder.get_doc_context(fromdocname, {}, {})

        context['feed_items'] = feed_items
        
        # Render the template
        feed_html = app.builder.templates.render('panels/rss.html.j2', context)
        
        new_node = nodes.raw('', feed_html, format='html')
        node.replace_self(new_node)


# ----------------------------------- SHARE PANEL


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
        
        html = app.builder.templates.render('panels/share.html.j2', {
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

# ----------------------------------- SHARE PANEL


def setup(app):
    """
    Register the directive and connect the event handler.
    """

    app.add_node(map_node)
    app.add_node(rss_node)
    app.add_node(share_node)

    app.add_directive('share', ShareDirective)
    app.add_directive('map', MapDirective)
    app.add_directive('rss', RssDirective)

    app.add_config_value('facebook_app_id', '', 'html') 
    app.add_config_value('google_maps_api_key', '', 'html')

    app.connect('doctree-resolved', process_share_nodes)
    app.connect('doctree-resolved', process_rss_nodes)
    app.connect('doctree-resolved', process_map_nodes)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }