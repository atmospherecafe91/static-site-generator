from textnode import TextNode, TextType
from helper_functions.split_nodes_delimiter import split_nodes_delimiter, split_array_delimiter, split_nodes_image, split_nodes_link


def text_to_textnodes(text: str) -> list[TextNode]:
    text_node = [TextNode(text, TextType.TEXT)]

    for delim, text_type in split_array_delimiter:
        text_node = split_nodes_delimiter(text_node, delim, text_type)
    
    text_node = split_nodes_image(text_node)
    text_node = split_nodes_link(text_node)

    return text_node
