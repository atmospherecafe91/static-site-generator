import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)
    
    def test_not_equal(self):
        node = TextNode("This is a text node that is differe", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertNotEqual(node, node2)        

    def test_url_exists(self):
        node = TextNode('This is a url', TextType.LINK, 'https://www.google.com')

        self.assertIsNotNone(node.url)

    def test_text(self):
        node = TextNode('This is a text node', TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, 'This is a text node')
    
    def test_it_returns_the_correct_tags(self):
        node = TextNode('This is a url', TextType.LINK, 'https://www.google.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">This is a url</a>')