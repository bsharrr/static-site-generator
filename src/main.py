from textnode import *
from htmlnode import *

def main():
    print(LeafNode("a", "This paragraph", {"href": "https://www.google.com"}).to_html())
    node = ParentNode(
         "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]
    )

    print(node.to_html())

if __name__=="__main__":
    main()