import unittest

from text_to_block import *


class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(markdown)
        expected_blocks = "[Block(['This is a heading'], BlockType.HEADING), Block(['This is a paragraph of text. It has some **bold** and *italic* words inside of it.'], BlockType.PARAGRAPH), Block(['This is a list item', 'This is another list item'], BlockType.UNORDERED_LIST)]"
        self.assertEqual(str(blocks), expected_blocks)


if __name__ == "__main__":
    unittest.main()
