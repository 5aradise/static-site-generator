import unittest

from text_to_node import *


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


class TestExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        found_images = extract_markdown_images(text)
        expected_images = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                           ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(found_images, expected_images)

    def test_extract_markdown_links(self):
        text = "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        found_images = extract_markdown_links(text)
        expected_images = [("link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                           ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(found_images, expected_images)


class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_new_nodes = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.BOLD,
        )
        node2 = TextNode(
            "This is text also with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)[second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and [third link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)!",
            TextType.ITALIC,
        )
        new_nodes = split_nodes_link([node, node2])
        expected_new_nodes = [
            TextNode("This is text with an ", TextType.BOLD),
            TextNode("link", TextType.LINK,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextType.BOLD),
            TextNode(
                "second link", TextType.LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
            TextNode("This is text also with an ", TextType.ITALIC),
            TextNode("link", TextType.LINK,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(
                "second link", TextType.LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
            TextNode(" and ", TextType.ITALIC),
            TextNode(
                "third link", TextType.LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
            TextNode("!", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)


if __name__ == "__main__":
    unittest.main()
