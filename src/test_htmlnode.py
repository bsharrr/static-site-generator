import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode



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

    
class TestParentNode(unittest.TestCase):

    def test_to_html_empty_tag(self):
        parent_node = ParentNode(tag=None, children=[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "The parent node needs a tag")


    def test_to_html_empty_children(self):
        parent_node = ParentNode(tag="p", children=None)
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "The parent node must contain at least a child")

    def test_to_html_one_child(self):
        parent_node = ParentNode(tag="p", children=[
        LeafNode("b", "Bold text"),
    ])
        
        self.assertEqual("<p><b>Bold text</b></p>", parent_node.to_html())

    def test_to_html_multiple_children(self):
        parent_node = ParentNode(tag="p", children=[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ])
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", parent_node.to_html())