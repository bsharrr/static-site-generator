from textnode import *
from htmlnode import *

def main():
    print(LeafNode("a", "This paragraph", {"href": "https://www.google.com"}).to_html())


if __name__=="__main__":
    main()