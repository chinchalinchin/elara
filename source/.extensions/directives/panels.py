import os
import re
import csv
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from urllib.parse import quote
import xml.etree.ElementTree as ET
from datetime import datetime
from io import StringIO

import folium
import numpy as np
import matplotlib

matplotlib.use('Agg') 

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from scipy.interpolate import make_interp_spline

# ----------------------------------- GRAPH PANEL
class graph_node(nodes.General, nodes.Element):
    """A custom node for graph charts to be replaced later."""
    pass

class GraphDirective(SphinxDirective):
    """
    Defines the .. graph:: directive to generate a scatterplot/spline.
    Accepts either an absolute/relative file path to a CSV or nested inline data.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 1 # Optional CSV file path
    final_argument_whitespace = True
    option_spec = {
        'width': directives.unchanged,
        'align': lambda arg: directives.choice(arg, ('left', 'center', 'right')),
        'interpolate': directives.flag,
        'title': directives.unchanged
    }

    def run(self):
        node = graph_node('')
        node['width'] = self.options.get('width', '100%')
        node['align'] = self.options.get('align', 'center')
        node['interpolate'] = 'interpolate' in self.options
        node['title'] = self.options.get('title')

        headers = []
        coords = []

        # 1. Prioritize File Argument
        if self.arguments:
            filepath = self.arguments[0].strip()
            if not os.path.isabs(filepath):
                # Resolve relative paths against the Sphinx source directory
                filepath = os.path.join(self.env.srcdir, filepath)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    headers = next(reader) # Assumes header row exists per requirements
                    coords = [row for row in reader if row]
            except Exception as e:
                return [self.state.document.reporter.error(
                    f"Graph Directive: Failed to read CSV {filepath} - {e}", line=self.lineno)]
        
        # 2. Fallback to Content Parsing
        else:
            current_row = []
            for line in self.content:
                line = line.strip()
                if line.startswith('* -'):
                    if current_row:
                        if not headers: 
                            headers = current_row
                        else: 
                            coords.append(current_row)
                    current_row = [line[3:].strip()]
                elif line.startswith('-') and current_row:
                    current_row.append(line[1:].strip())
            
            if current_row:
                if not headers: 
                    headers = current_row
                else: 
                    coords.append(current_row)

        if not coords or len(coords[0]) < 2:
            return [self.state.document.reporter.error(
                "Graph Directive: Insufficient data provided (requires at least 2 columns).", line=self.lineno)]

        node['headers'] = headers
        node['coords'] = coords
        return [node]


def process_graph_nodes(app, doctree, fromdocname):
    """
    Intercepts graph nodes, parses values (float vs datetime), generates a Matplotlib 
    SVG, and translates it to jinja HTML templates.
    """
    if app.builder.format != 'html':
        return
    
    for node in doctree.traverse(graph_node):
        coords = node.get('coords', [])
        headers = node.get('headers', ['X', 'Y'])
        title = node.get('title')
        
        if not coords:
            node.replace_self([])
            continue

        x_raw = [row[0] for row in coords]
        y_raw = [float(row[1]) for row in coords]

        # Determine if X-axis is Datetime or Float
        is_datetime = False
        try:
            x_vals = [float(v) for v in x_raw]
        except ValueError:
            try:
                # Naive ISO parser; replaces Z with standard UTC offset for compatibility
                x_vals = [datetime.fromisoformat(v.replace('Z', '+00:00')) for v in x_raw]
                is_datetime = True
            except ValueError:
                # TODO: Implement categorical x-axis if string data doesn't match isoformat
                app.logger.warning('Graph Directive: X-axis data could not be parsed as float or datetime.', location=node)
                node.replace_self([])
                continue

        # Convert to numeric arrays for robust manipulation and sorting
        if is_datetime:
            x_num = mdates.date2num(x_vals)
        else:
            x_num = np.array(x_vals)
            
        y_num = np.array(y_raw)

        # Sort data to prevent spline looping backwards 
        sort_idx = np.argsort(x_num)
        x_sorted = x_num[sort_idx]
        y_sorted = y_num[sort_idx]

        # Material UI Figure Setup
        fig, ax = plt.subplots(figsize=(8, 4.5))
        fig.patch.set_alpha(0.0) 
        ax.patch.set_alpha(0.0)

        # De-clutter Chart Junk
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('#999999')
        ax.spines['left'].set_color('#999999')
        ax.tick_params(colors='#999999')
        ax.grid(True, linestyle='--', alpha=0.15, color='#DDDDDD')
        
        # Apply Headers
        ax.set_xlabel(headers[0], color='#DDDDDD', fontsize=10, weight='medium')
        ax.set_ylabel(headers[1], color='#DDDDDD', fontsize=10, weight='medium')

        if title:
            # Padding pushes the title up slightly to prevent overlap with the chart area
            ax.set_title(title, color='#FFFFFF', fontsize=12, weight='bold', pad=15)

        # Format X-Axis if Datetime
        if is_datetime:
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
            fig.autofmt_xdate()

        # Execute Plotting
        if node.get('interpolate') and len(x_sorted) > 3:
            # Splines require strictly increasing independent variables
            x_unique, unique_idx = np.unique(x_sorted, return_index=True)
            y_unique = y_sorted[unique_idx]

            if len(x_unique) > 3:
                x_new = np.linspace(x_unique.min(), x_unique.max(), 300)
                spline = make_interp_spline(x_unique, y_unique, k=3)
                y_new = spline(x_new)

                # Convert numeric bounds back to datetime for matplotlib
                plot_x = mdates.num2date(x_new) if is_datetime else x_new
                
                # Plot Spline (Primary Deep Space Purple)
                ax.plot(plot_x, y_new, color='#9370DB', linewidth=2.5, alpha=0.9, zorder=2)

        # Always plot the raw scatter points (Secondary Galactic Blue)
        plot_scatter_x = [x_vals[i] for i in sort_idx] if is_datetime else x_sorted
        ax.scatter(plot_scatter_x, y_sorted, color='#42A5F5', s=35, zorder=3, edgecolors='#1E1E1E', linewidths=0.5)

        # Export Plot to SVG
        svg_buffer = StringIO()
        fig.savefig(svg_buffer, format='svg', bbox_inches='tight', transparent=True)
        plt.close(fig)
        svg_html = svg_buffer.getvalue()

        # Render output component
        rendered_html = app.builder.templates.render('panels/graph.html', {
            'svg_html': svg_html,
            'width': node['width'],
            'align': node['align']
        })
        
        new_node = nodes.raw('', rendered_html, format='html')
        node.replace_self(new_node)

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
    app.add_node(graph_node)

    app.add_directive('share', ShareDirective)
    app.add_directive('map', MapDirective)
    app.add_directive('rss', RssDirective)
    app.add_directive('verse', VerseDirective)
    app.add_directive('graph', GraphDirective)

    app.add_config_value('facebook_app_id', '', 'html') 

    app.connect('doctree-resolved', process_share_nodes)
    app.connect('doctree-resolved', process_rss_nodes)
    app.connect('doctree-resolved', process_map_nodes)
    app.connect('doctree-resolved', process_verse_nodes)
    app.connect('doctree-resolved', process_graph_nodes)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }