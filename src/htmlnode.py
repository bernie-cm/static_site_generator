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
        """Raises NotImplementedError to be implemented by child classes.
        Child classes will override this method to render themselves as HTML.
        """
        raise NotImplementedError
    
    def props_to_html(self):
        """Return a string that represents the HTML attributes of the node
        For example, if self.props is
        {"href": "https://www.google.com", "target": "_blank"}
        Then self.props_to_html() should return href="https://www.google.com" target="blank"
        """
        result = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {result}"
    
    def __repr__(self):
        """Prints a HTMLNode object and see its tag, value, children and props.
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    """Create a child class of HTMLNode called LeafNode. 
    Its constructor should differ slightly from the HTMLNode class because:
        - It should not allow for any children because leaf nodes are terminal nodes
        - The value data member should be required (and tag even though the tag's value may be None)
        - Use the super() function to call the constructor of the HTMLNode class."""
    def __init__(self, tag, value, props):
        if value is None:       # This ensures value is always required
            raise ValueError("LeafNode requires a value.")
        
        # Explicitly set children to an empty list as LeafNode cannot have children
        super().__init__(tag, value, children=[], props=props)

    def to_html(self):
        """Renders a leaf node as an HTML string (by returning a string).
        If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
        If there is no tag (e.g. it's None), the value should be returned as raw text.
        Otherwise, it should render an HTML tag. For example, these leaf nodes:
            LeafNode("p", "This is a paragraph of text.")
            LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        Should render as:
            <p>This is a paragraph of text.</p>
            <a href="https://www.google.com">Click me!</a>"""
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        
        # If  props is not empty, then call the props_to_html method to build the resulting string
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        # If props is empty
        # Take the tag and value from the constructor
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    """Create another child class of the HTMLNode called ParentNode. Its constructor should differ from the parent class in that:
    The tag and children arguments are not optional
    It doesn't take a value argument
    props is optional
    """
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Object must have a tag.")
        if self.children is None:
            raise ValueError("Children must be included.")
        
        # Recursively generate HTML for each child
        children_html = "".join(child.to_html() for child in self.children)
        
        return f"<{self.tag}>{children_html}</{self.tag}>"