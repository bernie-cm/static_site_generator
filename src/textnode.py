from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextType):
        raise Exception("text_node should be a valid type.")
    
    if text_node == TextType.TEXT:
        return LeafNode(tag=None, value=text_node)  # Raw text value with no tag
    if text_node == TextType.BOLD:
        pass
    if text_node == TextType.ITALIC:
        pass
    if text_node == TextType.CODE:
        pass
    if text_node == TextType.LINK:
        pass
    if text_node == TextType.IMAGE:
        pass