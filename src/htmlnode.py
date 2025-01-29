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

    
