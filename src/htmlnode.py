from typing import Self

class HTMLNode:
    def __init__(self, tag: str = None, value: str | None = None, children: dict[str, Self | None] = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ''
        
        return ''.join([f' {key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return(
            f'tag: {self.tag}\nvalue: {self.value}\nchildren: {print(self.children) if self.children is not None else 'None'}\nprops: {self.props}'
        )
    

class LeafNode(HTMLNode):

    def __init__(self, tag: str, value: str, props: dict[str, str] = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return(
            f'tag: {self.tag}\nvalue: {self.value}\nprops: {self.props}'
        )


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: dict[str, HTMLNode], props: str = None):
        super().__init__(tag=tag, children=children, props=props)
        self.children = children
        self.tag = tag
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError
        elif self.children is None:
            raise ValueError

        return f'<{self.tag}>{''.join([child.to_html() for child in self.children ])}</{self.tag}>'

