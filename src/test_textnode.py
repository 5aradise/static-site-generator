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
        html_node = text_node_to_html_node(text_node)
        expected_html = "Just text"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_converter2(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        expected_html = "<i>Italic text</i>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_converter3(self):
        text_node = TextNode("image", TextType.IMAGE, "boot.dev/cat.png")
        html_node = text_node_to_html_node(text_node)
        expected_html = '<img src="boot.dev/cat.png" alt="image"></img>'
        self.assertEqual(html_node.to_html(), expected_html)


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split(self):
        node = TextNode(
            "This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_new_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split2(self):
        try:
            node = TextNode(
                "This is text with a `code block` word`", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        except Exception as e:
            self.assertIsInstance(e, Exception)

    def test_split3(self):
        node = TextNode(
            "**bold text**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = [
            TextNode("bold text", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split4(self):
        node = TextNode(
            "*italic text 1* bold text *italic text 2*", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_new_nodes = [
            TextNode("italic text 1", TextType.ITALIC),
            TextNode(" bold text ", TextType.BOLD),
            TextNode("italic text 2", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)


if __name__ == "__main__":
    unittest.main()
