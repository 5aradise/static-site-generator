import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
