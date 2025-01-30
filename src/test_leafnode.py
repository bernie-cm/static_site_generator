import unittest
from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType

"""Create a few nodes and make sure the props_to_html method works 
as expected
"""
class TestLeafNode(unittest.TestCase):
    def test_renders_text_without_tag(self):
        """If tag is None, LeafNode should return raw text."""
        node = LeafNode(None, "Just some text", {})
        self.assertEqual(node.to_html(), "Just some text")

    def test_renders_simple_tag(self):
        """LeafNode should correctly wrap value in an HTML tag."""
        node = LeafNode("p", "Hello, world!", {})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_renders_tag_with_attributes(self):
        """LeafNode should include attributes in the rendered HTML."""
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()