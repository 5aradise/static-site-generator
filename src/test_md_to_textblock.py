import unittest

from md_to_textblock import *


class TestMdToTextBlocks(unittest.TestCase):
    def test_md_to_textblocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""
        blocks = md_to_textblocks(markdown)
        expected_blocks = [TextBlock(['This is a heading'], BlockType.HEADING),
                           TextBlock(['This is a paragraph of text. It has some **bold** and *italic* words inside of it.'],
                                 BlockType.PARAGRAPH),
                           TextBlock(['This is a list item', 'This is another list item'], BlockType.UNORDERED_LIST)]
        self.assertEqual(blocks, expected_blocks)


if __name__ == "__main__":
    unittest.main()
