import os
import re
import folium
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from urllib.parse import quote
import xml.etree.ElementTree as ET
from datetime import datetime

# ----------------------------------- VERSE PANEL
class verse_node(nodes.General, nodes.Element):
    """A custom node for the verse directive."""
    pass

class VerseDirective(SphinxDirective):
    """
    Defines the .. verse:: directive.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'increment': directives.positive_int,
    }

    def run(self):
        node = verse_node('')
        node['increment'] = self.options.get('increment', 0)
        
        # Parse each line for inline markup (like footnotes) so Sphinx registers them
        for text in self.content:
            line_node = nodes.inline('', '', classes=['verse-line-content'])
            if text.strip():
                text_nodes, messages = self.state.inline_text(text, self.lineno)
                line_node.extend(text_nodes)
                node += messages # Append system messages/errors directly to the parent node
            else:
                # Prevent the browser from collapsing the empty line
                line_node += nodes.Text('\u00A0')
                
            node.append(line_node)
            
        return [node]


def process_verse_nodes(app, doctree, fromdocname):
    """
    Finds all `verse_node` instances and replaces them with HTML.
    """
    if app.builder.format != 'html':
        return

    for node in doctree.traverse(verse_node):
        increment = node.get('increment', 0)
        processed_lines = []
        
        # Isolate the line nodes and system messages
        lines = [c for c in node.children if isinstance(c, nodes.inline) and 'verse-line-content' in c['classes']]
        messages = [c for c in node.children if isinstance(c, nodes.system_message)]
        
        line_count = 1
        
        # Enumerate through the lines, using Sphinx's native partial rendering
        for child in lines:
            # Check if this line is just the non-breaking space we injected for blank lines
            is_blank = len(child) == 1 and isinstance(child[0], nodes.Text) and child[0].astext() == '\u00A0'
            
            if increment and not is_blank and (line_count % increment == 0):
                number = str(line_count)
            else:
                number = ""
                
            if not is_blank:
                line_count += 1
            
            # Use render_partial to properly translate docutils nodes (like footnotes) into HTML strings
            rendered = app.builder.render_partial(child)
            
            # Handle cross-version compatibility (Sphinx 9.1+ changed the return key to 'fragment')
            line_html = rendered.get('fragment', rendered.get('body', ''))
            
            processed_lines.append({
                'text': line_html,
                'number': number
            })
            
        html = app.builder.templates.render('panels/verse.html', {
            'lines': processed_lines
        })
        
        new_node = nodes.raw('', html, format='html')
        # Replace the custom node with the rendered HTML and preserve any Sphinx system messages
        node.replace_self([new_node] + messages)
        
# ----------------------------------- MAPS PANEL

class map_node(nodes.General, nodes.Element):
    """A custom node for maps to be replaced later."""
    pass

class MapDirective(SphinxDirective):
    """
    Defines the .. map:: directive to generate a folium map with coordinate markers.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'width': directives.unchanged,
        'align': lambda arg: directives.choice(arg, ('left', 'center', 'right')),
        'interpolate': directives.flag
    }

    def run(self):
        node = map_node('')
        node['width'] = self.options.get('width', '100%')
        node['align'] = self.options.get('align', 'center')
        node['interpolate'] = 'interpolate' in self.options
        
        # Structurally parse coordinate pairs and optional labels 
        coords = []
        current_coord = None
        
        for line in self.content:
            line = line.strip()
            # New row triggered by '* -'
            if line.startswith('* -'):
                if current_coord is not None and 'lat' in current_coord and 'lon' in current_coord:
                    coords.append(current_coord)
                try:
                    current_coord = {'lat': float(line[3:].strip())}
                except ValueError:
                    current_coord = None 
            # Sequential columns in the row triggered by '-'
            elif line.startswith('-') and current_coord is not None:
                val = line[1:].strip()
                if 'lon' not in current_coord:
                    try:
                        current_coord['lon'] = float(val)
                    except ValueError:
                        pass 
                elif 'label' not in current_coord:
                    current_coord['label'] = val
                    
        # Append the final item if valid
        if current_coord is not None and 'lat' in current_coord and 'lon' in current_coord:
            coords.append(current_coord)
            
        node['coords'] = coords
        return [node]

def process_map_nodes(app, doctree, fromdocname):
    """
    Intercepts map nodes, computes bounds, generates Folium iframes, 
    and translates them to jinja HTML templates.
    """
    if app.builder.format != 'html':
        return
    
    for node in doctree.traverse(map_node):
        coords = node.get('coords', [])
        
        # Omit block if there are no coordinates provided
        if not coords:
            node.replace_self([])
            continue
            
        lats = [c['lat'] for c in coords]
        lons = [c['lon'] for c in coords]
        
        center_lat = sum(lats) / len(lats)
        center_lon = sum(lons) / len(lons)
        
        # Handle single pin vs multi-pin maps
        if len(coords) == 1:
            m = folium.Map(location=[center_lat, center_lon], zoom_start=12)
            item = coords[0]
            folium.Marker(
                [item['lat'], item['lon']],
                tooltip=item.get('label')
            ).add_to(m)
        else:
            m = folium.Map(location=[center_lat, center_lon])
            
            # Apply linear interpolation path if requested
            if node.get('interpolate'):
                points = [[c['lat'], c['lon']] for c in coords]
                folium.PolyLine(
                    points, 
                    color="#9370DB", 
                    weight=3.5, 
                    opacity=0.85
                ).add_to(m)
            
            for item in coords:
                folium.Marker(
                    [item['lat'], item['lon']],
                    tooltip=item.get('label')
                ).add_to(m)
                
            sw = [min(lats), min(lons)]
            ne = [max(lats), max(lons)]
            # Fit bounds with a comfortable padding margin
            m.fit_bounds([sw, ne], padding=(50, 50))
            
        # Render the full Folium iFrame HTML
        map_html = m._repr_html_()
        
        rendered_html = app.builder.templates.render('panels/map.html', {
            'map_html': map_html,
            'width': node['width'],
            'align': node['align']
        })
        
        new_node = nodes.raw('', rendered_html, format='html')
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
                        # Attempt to parse RFC 822 format, ignoring the timezone abbreviation
                        pub_date_no_tz = pub_date_str.rsplit(' ', 1)[0]
                        dt_object = datetime.strptime(pub_date_no_tz, '%a, %d %b %Y %H:%M:%S')
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
        feed_html = app.builder.templates.render('panels/rss.html', context)
        
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
        facebook_icon_path = os.path.relpath('.static/svg/facebook.svg', from_dir).replace(os.path.sep, '/')
        twitter_icon_path = os.path.relpath('.static/svg/x.svg', from_dir).replace(os.path.sep, '/')
        instagram_icon_path = os.path.relpath('.static/svg/instagram.svg', from_dir).replace(os.path.sep, '/')
        
        html = app.builder.templates.render('panels/share.html', {
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

# ----------------------------------- SETUP ROUTING

def setup(app):
    """
    Register the directive and connect the event handler.
    """

    app.add_node(map_node)
    app.add_node(rss_node)
    app.add_node(share_node)
    app.add_node(verse_node)

    app.add_directive('share', ShareDirective)
    app.add_directive('map', MapDirective)
    app.add_directive('rss', RssDirective)
    app.add_directive('verse', VerseDirective)

    app.add_config_value('facebook_app_id', '', 'html') 

    app.connect('doctree-resolved', process_share_nodes)
    app.connect('doctree-resolved', process_rss_nodes)
    app.connect('doctree-resolved', process_map_nodes)
    app.connect('doctree-resolved', process_verse_nodes)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }