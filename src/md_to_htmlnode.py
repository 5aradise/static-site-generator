from htmlnode import *
from md_to_textblock import BlockType, md_to_textblocks
from textblock import textblock_to_htmlnode

def md_to_htmlnode(md: str) -> ParentNode:
    all_parent_nodes = list[ParentNode]()
    textblocks = md_to_textblocks(md)
    for textblock in textblocks:
        htmlnode = textblock_to_htmlnode(textblock)
        all_parent_nodes.append(htmlnode)
    return ParentNode("div", all_parent_nodes)
