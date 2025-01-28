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

    def test_url_not_eq(self):
        node_1 = TextNode("Test node", TextType.BOLD, "http://amazon.com.au")
        node_2 = TextNode("Test node", TextType.BOLD, "http://github.com")
        self.assertNotEqual(node_1.url, node_2.url)

    def test_two_attributes_not_eq(self):
        node_1 = TextNode("Text node 1", TextType.IMAGE, "https://github.com")
        node_2 = TextNode("Text node 2", TextType.BOLD, "htts://github.com")
        self.assertNotEqual(node_1, node_2)
        


if __name__ == "__main__":
    unittest.main()