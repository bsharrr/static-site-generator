class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props

    def to_html(self):
        pass
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = "" 
        for prop in self.props: 
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode ({self.tag}, {self.value}, {self.children}, {self.props})"
    




class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have value")
        if self.tag is None:
            return f"{self.value}"
        if self.tag == "a":
            prop = self.props_to_html()
            return f"<a{prop}>{self.value}</a>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    


class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag=tag, children=children)
   
    def to_html(self):
        if self.tag is None:
            raise ValueError("The parent node needs a tag")
        if self.children is None:
            raise ValueError("The parent node must contain at least a child")
        children = ""
        for child in self.children:
            child = str(child.to_html())
            children += child

        return f"<{self.tag}>{children}</{self.tag}>"


        
        
            
        


    