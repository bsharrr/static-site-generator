from textnode import *

def main():
    test = TextNode("This is the test", TextType.NORMAL.value, "https://www.google.com")
    print(test)


if __name__=="__main__":
    main()