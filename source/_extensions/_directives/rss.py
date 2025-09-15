import os
import xml.etree.ElementTree as ET
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from datetime import datetime

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
        feed_html = app.builder.templates.render('widgets/rss.html', context)
        
        new_node = nodes.raw('', feed_html, format='html')
        node.replace_self(new_node)

def setup(app):
    """Register the directive and connect the event handler."""
    app.add_node(rss_node)
    app.add_directive('rss', RssDirective)
    app.connect('doctree-resolved', process_rss_nodes)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }