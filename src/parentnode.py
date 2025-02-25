from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("ParentNode tag cannot be None or empty")
        if self.children is None or self.children == []:
            raise ValueError("ParentNode children cannot be None or empty")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"

    def __repr__(self):
        return f"ParenNode({self.tag}, {self.children}, {self.props})"
