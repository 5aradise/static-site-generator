from enum import Enum


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


block_type_marks = {
    BlockType.HEADING: "#",
    BlockType.CODE: "```",
    BlockType.QUOTE: "> ",
    BlockType.UNORDERED_LIST: "* ",
    BlockType.ORDERED_LIST: ". "
}

headind_types = [BlockType.HEADING, BlockType.HEADING2, BlockType.HEADING3,
                 BlockType.HEADING4, BlockType.HEADING5, BlockType.HEADING6]


class Block:
    def __init__(self, text: str):
        self.body = [text]
        self.type = BlockType.PARAGRAPH

        for i in range(6, 0, -1):
            if text.startswith(block_type_marks[BlockType.HEADING]*i+" "):
                self.body = [text[i+1:]]
                self.type = headind_types[i-1]
                return

        if text.startswith(block_type_marks[BlockType.CODE]) and text.endswith(block_type_marks[BlockType.CODE]):
            self.body = [text[len(block_type_marks[BlockType.CODE]):]]
            self.type = BlockType.CODE
            return

        if text.startswith(block_type_marks[BlockType.QUOTE]):
            isQuote = True
            text_lines = text.split("\n")
            quote_lines = list[str]()
            for text_line in text_lines:
                if not text_line.startswith(block_type_marks[BlockType.QUOTE]):
                    isQuote = False
                    break
                else:
                    quote_lines.append(text_line[len(block_type_marks[BlockType.QUOTE]):])

            if isQuote:
                self.body = quote_lines
                self.type = BlockType.QUOTE
                return

        if text.startswith(block_type_marks[BlockType.UNORDERED_LIST]):
            isList = True
            text_lines = text.split("\n")
            list_lines = list[str]()
            for text_line in text_lines:
                if not text_line.startswith(block_type_marks[BlockType.UNORDERED_LIST]):
                    isList = False
                    break
                else:
                    list_lines.append(text_line[len(block_type_marks[BlockType.UNORDERED_LIST]):])

            if isList:
                self.body = list_lines
                self.type = BlockType.UNORDERED_LIST
                return

        if text.startswith(str(1) + block_type_marks[BlockType.ORDERED_LIST]):
            isList = True
            text_lines = text.split("\n")
            list_lines = list[str]()
            for i in range(1, len(text_lines)+1):
                if not text_lines[i-1].startswith(str(i)+block_type_marks[BlockType.ORDERED_LIST]):
                    isList = False
                    break
                else:
                    list_lines.append(text_lines[i-1][1 + len(block_type_marks[BlockType.ORDERED_LIST]):])

            if isList:
                self.body = list_lines
                self.type = BlockType.ORDERED_LIST
                return

    def __eq__(self, other: 'Block') -> bool:
        return (self.body == other.body
                and self.type == other.type)

    def __repr__(self) -> str:
        return f"Block({self.body}, {self.type})"


def markdown_to_blocks(markdown: str) -> list[Block]:
    blocks = list[Block]()
    text_blocks = markdown.split("\n\n")
    for text_block in text_blocks:
        if text_block != "":
            blocks.append(Block(text_block))
    return blocks