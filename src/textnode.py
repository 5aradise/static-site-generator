from enum import Enum
from htmlnode import *


class TextType(Enum):
    TEXT = 0
    BOLD = 1
    ITALIC = 2
    CODE = 3
    LINK = 4
    IMAGE = 5


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        if text_type not in TextType:
            raise Exception("unknown text type")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: 'TextNode') -> bool:
        return (self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = list[TextType]()
    for old_node in old_nodes:
        if type(old_node) is not TextNode:
            new_nodes.append(old_node)

        splited_text = old_node.text.split(delimiter)
        text_types = [old_node.text_type, text_type]

        if len(splited_text) % 2 != 1:
            raise Exception("matching closing delimeter is not found")
        for switcher in range(len(splited_text)):
            if not splited_text[switcher]:
                continue

            new_node = TextNode(
                splited_text[switcher], text_types[switcher % 2])
            new_nodes.append(new_node)

    return new_nodes
