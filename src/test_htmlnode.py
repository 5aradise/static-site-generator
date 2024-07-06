import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="img", props={
                        "src": "url/of/image.png", "alt": "Description of image"})
        expected_html_props = ' src="url/of/image.png" alt="Description of image"'
        self.assertEqual(node.props_to_html(), expected_html_props)

    def test_props_to_html2(self):
        node = HTMLNode(tag="img", props={
                        "href": "https://www.google.com", "target": "_blank"})
        expected_html_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html_props)

    def test_props_to_html3(self):
        node = HTMLNode(tag="img")
        expected_html_props = ""
        self.assertEqual(node.props_to_html(), expected_html_props)


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]],
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html2(self):
        node = ParentNode(
            "p",
            [[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [[
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]],
                ),
            ]],
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html3(self):
        try:
            node = ParentNode(
                "p",
                [],
            )
            node.to_html()
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_to_html4(self):
        node = ParentNode(
            "p",
            [[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [[
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]],
                    {"alt": "Description of image"}
                ),
            ]],
            {"href": "https://www.google.com", "target": "_blank"}
        )
        expected_html = '<p href="https://www.google.com" target="_blank"><b>Bold text</b>Normal text<a href="https://www.google.com">Click me!</a>Normal text<p alt="Description of image"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>'
        self.assertEqual(node.to_html(), expected_html)


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
