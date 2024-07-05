from enum import Enum
from textblock import *


block_type_marks = {
    BlockType.HEADING: "#",
    BlockType.CODE: "```",
    BlockType.QUOTE: "> ",
    BlockType.UNORDERED_LIST: "* ",
    BlockType.ORDERED_LIST: ". "
}

headind_types = [BlockType.HEADING, BlockType.HEADING2, BlockType.HEADING3,
                 BlockType.HEADING4, BlockType.HEADING5, BlockType.HEADING6]


def md_to_textblocks(markdown: str) -> list[TextBlock]:
    blocks = list[TextBlock]()
    md_blocks = markdown.split("\n\n")
    for md_block in md_blocks:
        if md_block != "":
            blocks.append(md_to_textblock(md_block))
    return blocks


def md_to_textblock(md: str) -> TextBlock:
    for i in range(6, 0, -1):
        if md.startswith(block_type_marks[BlockType.HEADING]*i+" "):
            return TextBlock([md[i+1:]], headind_types[i-1])

    if md.startswith(block_type_marks[BlockType.CODE]) and md.endswith(block_type_marks[BlockType.CODE]):
        return TextBlock([md[len(block_type_marks[BlockType.CODE]):]], BlockType.CODE)

    if md.startswith(block_type_marks[BlockType.QUOTE]):
        isQuote = True
        md_lines = md.split("\n")
        quote_lines = list[str]()
        for md_line in md_lines:
            if not md_line.startswith(block_type_marks[BlockType.QUOTE]):
                isQuote = False
                break
            else:
                quote_lines.append(
                    md_line[len(block_type_marks[BlockType.QUOTE]):])

        if isQuote:
            return TextBlock(quote_lines, BlockType.QUOTE)

    if md.startswith(block_type_marks[BlockType.UNORDERED_LIST]):
        isList = True
        md_lines = md.split("\n")
        list_lines = list[str]()
        for md_line in md_lines:
            if not md_line.startswith(block_type_marks[BlockType.UNORDERED_LIST]):
                isList = False
                break
            else:
                list_lines.append(
                    md_line[len(block_type_marks[BlockType.UNORDERED_LIST]):])
        if isList:
            return TextBlock(list_lines, BlockType.UNORDERED_LIST)

    if md.startswith(str(1) + block_type_marks[BlockType.ORDERED_LIST]):
        isList = True
        md_lines = md.split("\n")
        list_lines = list[str]()
        for i in range(1, len(md_lines)+1):
            if not md_lines[i-1].startswith(str(i)+block_type_marks[BlockType.ORDERED_LIST]):
                isList = False
                break
            else:
                list_lines.append(
                    md_lines[i-1][1 + len(block_type_marks[BlockType.ORDERED_LIST]):])

        if isList:
            return TextBlock(list_lines, BlockType.ORDERED_LIST)
    return TextBlock([md], BlockType.PARAGRAPH)
