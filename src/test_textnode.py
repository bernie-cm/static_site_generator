import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("Test node", TextType.NORMAL)
        node2 = TextNode("Test node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("This is a test node", TextType.ITALIC, "http://google.com")
        self.assertIsNotNone(node.url)


"""
Add even more test cases (at least 3 in total) to check various edge cases, 
like when the url property is None, or when the text_type property is different. 
You'll want to make sure that when properties are different, the TextNode 
objects are not equal.
"""


if __name__ == "__main__":
    unittest.main()