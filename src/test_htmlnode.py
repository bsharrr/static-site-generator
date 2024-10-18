import unittest
from htmlnode import HTMLNode, LeafNode



class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "test", None, {"href": "https://www.google.com"})
        self.assertEqual(' href="https://www.google.com"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode("p", "test", None, {"href": "https//:www.google.com"})
        self.assertEqual("HTMLNode (p, test, None, {'href': 'https//:www.google.com'})", repr(node))


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', str(leaf.to_html()))
    
    def test_to_html_empty_tag(self):
        leaf = LeafNode(tag=None, value="This is a text", props=None)
        self.assertEqual("This is a text", leaf.to_html())

    def test_to_html_empty_tag(self):
        leaf = LeafNode(tag="p", value=None, props={"href": "https://www.google.com"})
        with self.assertRaises(ValueError) as context:
            leaf.to_html()
        self.assertEqual(str(context.exception), "All leaf nodes must have value")

    