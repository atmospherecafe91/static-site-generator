import re

from enum import Enum

from textnode import TextNode, TextType
from helper_functions.extract_markdown import extract_markdown_images, extract_markdown_links


split_array_delimiter = [
    ('**', TextType.BOLD),
    ('_', TextType.ITALIC),
    ('`', TextType.CODE)
]

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    
    new_node = list()

    

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_node.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                raise Exception(f'Error - No matching delimiter found for {text_type}')
            
            split_node = [ TextNode(value, TextType.TEXT) if i % 2 == 0 else TextNode(value, text_type)  for i, value in enumerate(node.text.split(delimiter))]


            new_node.extend(list(filter(lambda x: x.text != '', split_node)))
            
    return new_node


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_node = list()
    split_node(old_nodes, new_node, TextType.IMAGE)
    return new_node  

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_node = list()
    split_node(old_nodes, new_node, TextType.LINK)
    return new_node     


def split_node(old_nodes: list[TextNode], new_node: list[TextNode], type: TextType) -> list[TextNode]:

    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_node.append(node)
        else:
            split_list = []

            if type == TextType.IMAGE:
                split_list.extend(extract_markdown_images(node.text))
            elif type == TextType.LINK:
                split_list.extend(extract_markdown_links(node.text))
            else:
                raise Exception('Error - split type not found')
            
            
            t_text = node.text
            
            for key, value in split_list:
                temp = t_text.split(f'{'!' if type == TextType.IMAGE else ''}[{key}]({value})')
                text_node = temp.pop(0)
                
                if text_node:
                    new_node.extend([TextNode(text_node, TextType.TEXT), TextNode(key, type, value)])
                else:
                    new_node.append(TextNode(key, type, value))

                t_text = ''.join(temp)

            if t_text:
                new_node.append(TextNode(t_text, TextType.TEXT))



