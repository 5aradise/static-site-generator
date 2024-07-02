from htmlnode import *
from text_to_block import BlockType, markdown_to_blocks
from text_to_node import text_to_textnodes
from textnode import textnode_to_htmlnode

tag_block_type = {
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

def markdown_to_html_node(markdown: str) -> ParentNode:
    all_parent_nodes = list[ParentNode]()
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        curr_leaf_nodes = list[LeafNode]()
        for text in block.body:
            text_nodes = text_to_textnodes(text)
            for text_node in text_nodes:
                html_node = textnode_to_htmlnode(text_node)
                curr_leaf_nodes.append(html_node)
            all_parent_nodes.append(ParentNode(tag_block_type[block.type], curr_leaf_nodes))
    return ParentNode("div", all_parent_nodes)
