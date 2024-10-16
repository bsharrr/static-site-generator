import unittest
from htmlnode import HTMLNode



class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "test", None, {"href": "https://www.google.com"})
        self.assertEqual(' href="https://www.google.com"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode("p", "test", None, {"href": "https//:www.google.com"})
        self.assertEqual("HTMLNode (p, test, None, {'href': 'https//:www.google.com'})", repr(node))
        