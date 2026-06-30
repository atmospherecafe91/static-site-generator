from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    TEXT = "text"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url = None):
        self.text = text 
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, text_node: "TextNode"):
        return self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
    

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, { "href": text_node.url })
        case TextType.IMAGE:
            return LeafNode('img', '', { "src": text_node.url, "alt": text_node.text })
        case _:
            raise Exception('TextType has to match one of the enum types')