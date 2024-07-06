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
    def __init__(self, text: str, type: TextType, url: str = None):
        if type not in TextType:
            raise Exception("unknown text type")

        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, other: 'TextNode') -> bool:
        return (self.text == other.text
                and self.type == other.type
                and self.url == other.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def textnode_to_htmlnode(textnode: TextNode) -> LeafNode:
    match textnode.type:
        case TextType.TEXT:
            return LeafNode(None, textnode.text)
        case TextType.BOLD:
            return LeafNode("b", textnode.text)
        case TextType.ITALIC:
            return LeafNode("i", textnode.text)
        case TextType.CODE:
            return LeafNode("code", textnode.text)
        case TextType.LINK:
            return LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})
