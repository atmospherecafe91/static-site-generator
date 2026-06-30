from unittest import TestCase
from helper_functions.split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNode(TestCase):

    def test_it_returns_the_correct_node_length(self):
        node = TextNode("`code block` word", TextType.TEXT)

        res = split_nodes_delimiter([node], '`', TextType.CODE)

        self.assertEqual(len(res), 2, msg=res)

        node = TextNode("This is text with a `code block` word", TextType.TEXT)

        self.assertEqual(len(split_nodes_delimiter([node], '`', TextType.CODE)), 3)

    
    def test_it_return_error_when_given_non_matching_tags(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], '`', TextType.CODE)