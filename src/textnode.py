from enum import Enum

# Enum called TextType
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # Create an __eq__ method that returns True if all 
    # of the properties of two TextNode objects are equal
    def __eq__(self, other):
        # Check if the other object is an instance of the
        # same class TextNode
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url
        )
    
    # Create a __repr__ method that returns a string 
    # representation of the TextNode object
    def __repr__ (self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"