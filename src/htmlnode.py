class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # Represents the HTML tag name
        self.value = value          # Represents the value of the HTML tag, i.e. text inside a <p>
        self.children = children    # List of HTMLNode objects
        self.props = props          # Dict representing the attributes of the HTML tag

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
