from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # Represents the HTML tag name
        self.value = value          # Represents the value of the HTML tag, i.e. text inside a <p>
        self.children = children    # List of HTMLNode objects
        self.props = props          # Dict representing the attributes of the HTML tag

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {result}"
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:       # This ensures value is always required
            raise ValueError("LeafNode requires a value.")  
        # Explicitly set children to an empty list as LeafNode cannot have children
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        # If  props is not empty, then call the props_to_html method to build the resulting string
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Object must have a tag.")
        if self.children is None:
            raise ValueError("Children must be included.")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    

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