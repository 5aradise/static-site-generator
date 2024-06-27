class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: 'HTMLNode' = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        htmled_props = ""
        for (k, v) in self.props.items():
            htmled_props += f' {k}="{v}"'
        return htmled_props

    def __repr__(self) -> str:
        return f"HTMLNode(tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"
