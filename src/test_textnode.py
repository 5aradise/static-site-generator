import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node",  TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node",  TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_type(self):
        try:
            node = TextNode("Untyped node", "line")
        except Exception as e:
            self.assertIsInstance(e, Exception)


class TestTextNode(unittest.TestCase):
    def test_converter(self):
        text_node = TextNode("Just text", TextType.TEXT)
        html_node = textnode_to_htmlnode(text_node)
        expected_html = "Just text"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_converter2(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = textnode_to_htmlnode(text_node)
        expected_html = "<i>Italic text</i>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_converter3(self):
        text_node = TextNode("image", TextType.IMAGE, "boot.dev/cat.png")
        html_node = textnode_to_htmlnode(text_node)
        expected_html = '<img src="boot.dev/cat.png" alt="image">'
        self.assertEqual(html_node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
