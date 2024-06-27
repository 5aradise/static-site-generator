import unittest

from htmlnode import HTMLNode, LeafNode


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
