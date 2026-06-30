import re

from htmlnode import HTMLNode, ParentNode
from helper_functions.markdown_to_blocks import markdown_to_blocks
from helper_functions.block_types import block_to_block_type_fn, BlockTypes
from helper_functions.text_to_textnode import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def text_to_children(text):
    text_node = text_to_textnodes(text)

    html_text_node = []

    for node in text_node:
        html_text_node.append(text_node_to_html_node(node))
    
    return html_text_node

def filter_markdown(markdown_block: list[str]) -> list[str]:
    blocks = markdown_block.split('\n\n')
    filter_block = []

    for block in blocks:
        if block == '':
            continue
        filter_block.append(block.strip())
    
    return filter_block


def markdown_to_html_node(markdown_doc: str) -> HTMLNode:

    blocks = filter_markdown(markdown_doc)
    children_node = []

    for block in blocks:
        node = block_html_node(block)
        children_node.append(node)
    
    return ParentNode('div', children_node)


def block_html_node(block: str):

    block_type = block_to_block_type_fn(block)

    if block_type == BlockTypes.PARAGRAPH:
        return paragraph_html_node(block)
    elif block_type == BlockTypes.HEADING:
        return heading_html_node(block)
    elif block_type == BlockTypes.CODE:
        return code_html_node(block)
    elif block_type == BlockTypes.QUOTE:
        return quote_html_node(block)
    elif block_type == BlockTypes.ORDERED_LIST:
        return ordered_html_node(block)
    elif block_type == BlockTypes.UNORDERED_LIST:
        return unordered_html_node(block)
    else:
        raise Exception('Error - Couldn\'t find block node for specified block')

def unordered_html_node(block):

    lines = block.strip().split('\n')
    new_lines = []

    for line in lines:
        block_text = line.split('- ', 1)[1]
        block_text_node = text_to_children(block_text)
        new_lines.append(ParentNode('li', block_text_node))
    
    return ParentNode('ul', new_lines)

def ordered_html_node(block):
    lines = block.strip().split('\n')
    new_lines = []

    for line in lines:
        block_text = line.split('. ', 1)[1]
        block_text_node = text_to_children(block_text)
        new_lines.append(ParentNode('li', block_text_node))
    
    return ParentNode('ol', new_lines)
    


def quote_html_node(block):
    lines = block.split('\n')
    new_lines = []
    
    if not block.startswith('>'):
        raise ValueError(f'Invalid quote block')
    
    for line in lines:
        if not line.startswith('>'):
            raise ValueError(f'Invalid quote block')
        new_lines.append(line.lstrip('>').strip())
    
    block_text = ' '.join(new_lines)
    block_text_nodes = text_to_children(block_text)
    return ParentNode('blockquote', block_text_nodes)
    

def code_html_node(block):
    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError(f'Invalid code block')
    
    block_text = block[4:-3]
    block_text_node = text_node_to_html_node(TextNode(block_text, TextType.CODE))
    return ParentNode('pre', [block_text_node])



def heading_html_node(block: str):
    block_text = ''
    level = 0

    for char in block:
        if char == '#':
            level += 1
        else:
            break
    
    block_tag = f'h{level}'
    block_text = block[level:].strip()
    block_text_node = text_to_children(block_text)
    block_parent_node = ParentNode(block_tag, block_text_node)
    return block_parent_node

    

def paragraph_html_node(block: str):
    block_text = block.replace('\n', ' ').strip()
    block_text_node = text_to_children(block_text)
    block_parent_node = ParentNode('p', block_text_node)
  
    return block_parent_node