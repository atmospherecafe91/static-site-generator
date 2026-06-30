from unittest import TestCase
from htmlnode import HTMLNode

class TestHTMLNode(TestCase):
    
    def test_it_returns_correct_formatted_props(self):
        html_node = HTMLNode('a', 'testing link', None, { "href": 'https://www.google.com', "target": "_blank" })

        self.assertEqual(html_node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
    def test_it_returns_none_when_no_props(self):
        html_node = HTMLNode('a', 'testing link')
        self.assertEqual(html_node.props_to_html(), '')
    
    def test_it_returns_the_correct_tag(self):
        html_node = HTMLNode('a', 'testing link', None, { "href": 'https://www.google.com', "target": "_blank" })

        self.assertEqual(html_node.tag, 'a')

