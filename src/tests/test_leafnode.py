from unittest import TestCase

from htmlnode import LeafNode

class TestLeadNode(TestCase):

    def test_returns_error_if_no_value(self):
        lead_node = LeafNode('p', None)
        
        with self.assertRaises(ValueError):
            lead_node.to_html()
    
    def test_returns_the_correct_output_without_props(self):
        lead_node = LeafNode('p', 'testing links')

        self.assertEqual(lead_node.to_html(), '<p>testing links</p>')
    
    def test_returns_the_correct_output_with_props(self):
        lead_node = LeafNode('p', 'testing links', {"href": "https://www.google.com"})

        self.assertEqual(lead_node.to_html(), '<p href="https://www.google.com">testing links</p>')
        