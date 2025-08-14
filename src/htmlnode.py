class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        ans = ""
        for a, b in self.props.items():
            ans += f' {a}="{b}"'
        return ans
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Invalid HTML: there should be a value in a Leaf Node")
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTMl: there should be a tag in a Parent Node")
        if not self.children:
            raise ValueError("Invalid HTML: there should be children in a Parent Node")
        
        # recursively return the children
        return f"<{self.tag}{self.props_to_html()}>{"".join(child.to_html() for child in self.children)}</{self.tag}>"
