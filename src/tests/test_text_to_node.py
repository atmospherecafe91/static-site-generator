from unittest import TestCase

from helper_functions.text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType


class TestTextNode(TestCase):

    def test_it_returns_the_correct_node_list(self):
        text_str = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"



        self.assertEqual(
            text_to_textnodes(text_str),
            [
                TextNode("This is ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word and a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" and an ", TextType.TEXT), TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://boot.dev")
            ]
        )
