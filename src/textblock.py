from enum import Enum
from htmlnode import ParentNode
from textnode import textnode_to_htmlnode
from md_to_textnode import md_to_textnodes
from htmlnode import LeafNode

class BlockType(Enum):
    PARAGRAPH = 0
    HEADING = 1
    HEADING2 = 2
    HEADING3 = 3
    HEADING4 = 4
    HEADING5 = 5
    HEADING6 = 6
    CODE = 7
    QUOTE = 8
    UNORDERED_LIST = 9
    ORDERED_LIST = 10


class TextBlock:
    def __init__(self, body: list[str], type: BlockType):
        self.body = body
        self.type = type

    def __eq__(self, other: 'TextBlock') -> bool:
        return (self.body == other.body
                and self.type == other.type)

    def __repr__(self) -> str:
        return f"Block({self.body}, {self.type})"


block_type_tag = {
    BlockType.PARAGRAPH: "p",
    BlockType.HEADING: "h1",
    BlockType.HEADING2: "h2",
    BlockType.HEADING3: "h3",
    BlockType.HEADING4: "h4",
    BlockType.HEADING5: "h5",
    BlockType.HEADING6: "h6",
    BlockType.CODE: "code",
    BlockType.QUOTE: "blockquote",
    BlockType.UNORDERED_LIST: "ul",
    BlockType.ORDERED_LIST: "ol",
}


def textblock_to_htmlnode(textblock: TextBlock):
    leaf_nodes = list[LeafNode]()
    for md_line in textblock.body:
        textnodes = md_to_textnodes(md_line)
        for textnode in textnodes:
            htmlnode = textnode_to_htmlnode(textnode)
            leaf_nodes.append(htmlnode)
    return ParentNode(block_type_tag[textblock.type], leaf_nodes)
