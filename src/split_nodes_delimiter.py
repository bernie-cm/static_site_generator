from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:      # Each node will be a TextNode object with text_type attribute
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)  
            continue
        text = node.text    # This will get the text attribute of the TextNode object
        delimiter_index = text.find(delimiter)
        if delimiter_index == -1:
            # No delimiter found, keep the text as is
            new_nodes.append(node)
            continue
        # TODO: Find closing delimiter
        # TODO: Split into three parts
        # TODO: Create new nodes for each part


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url



    # Return new list of nodes "result"