class HtmlNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        value = ""
        if self.props != None:
            for k, v in self.props.items():
                value += f' {k}="{v}"'
            return value

    def __repr__(self):
        return f'HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return self.value
        if self.props != None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No HTML Tag Provided")
        if self.children == None:
            raise ValueError("No Child Nodes Provided")
        
        # contact all children into a string
        # wrap that string within the parent node tag

        childHtmlString = ""

        for child in self.children:
            childHtmlString += child.to_html()
        return f'<{self.tag}>{childHtmlString}</{self.tag}>'   

    def __repr__(self):
        return f'ParentNode({self.children}, {self.tag}, {self.props})'