class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list[list['HTMLNode']] = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""

        htmled_props = ""
        for (k, v) in self.props.items():
            htmled_props += f' {k}="{v}"'
        return htmled_props
    
    def __eq__(self, other: 'HTMLNode') -> bool:
        return (self.tag == other.tag
                and self.value == other.value
                and self.children == self.children
                and self.props == other.props)

    def __repr__(self) -> str:
        return f"HTMLNode(tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[list[HTMLNode]], props: dict = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes require a tag")

        if len(self.children) == 0:
            raise ValueError("Parent node must have at least one child")
        
        list_tags = ["ul", "ol"]
        
        is_list = self.tag in list_tags
        htmled_node = f"<{self.tag}{self.props_to_html()}>"
        for child_line in self.children:
            htmled_child_line = ""
            for child in child_line:
                htmled_child_line += child.to_html()
            htmled_node += f"<li>{htmled_child_line}</li>" if is_list else htmled_child_line
        htmled_node += f"</{self.tag}>"

        return htmled_node


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
