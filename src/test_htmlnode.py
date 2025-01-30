import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType

"""Create a few nodes and make sure the props_to_html method works 
as expected
"""
class TestHTMLNode(unittest.TestCase):
    
    def test_eq(self):
        node_1 = HTMLNode()
        node_2 = HTMLNode()
        self.assertEqual(node_1, node_2)
    
    def test_eq_not_implemented(self):
        node_1 = HTMLNode()
        node_2 = TextNode("Test node", TextType.IMAGE, "https://google.com")
        self.assertNotIsInstance
    
    def test_props_to_html(self):
        node_1 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node_1.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()