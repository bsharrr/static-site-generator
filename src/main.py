from textnode import *
from htmlnode import *

def main():
    test = TextNode("This is the test", TextType.NORMAL, "https://www.google.com")
    htmltest = HTMLNode("p", "test", None, {
         "href": "https://www.google.com", 
        "target": "_blank"
    })

    print(htmltest.props_to_html())


if __name__=="__main__":
    main()