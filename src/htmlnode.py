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
        {
            "href": "https://www.google.com",
            "target": "_blank",
        }
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
        - Use the super() function to call the constructor of the HTMLNode class.
    """
    def __init__(self, tag, value, props):
        if value is None:       # This ensures value is always required
            raise ValueError("LeafNode requires a value.")
        
        super().__init__(tag, value, children=[], props=props)
        # TODO: Define following methods and tests
