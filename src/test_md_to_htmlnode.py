import unittest

from md_to_htmlnode import *


class TestMdToHTMLNode(unittest.TestCase):
    def test_md_to_htmlnode(self):
        markdown = """# Sample Markdown

This is some basic, sample markdown.

## Second Heading

### Unordered lists:

* One
* Two
* Three

### Ordered lists:

1. One
2. Two
3. Three

> Blockquote
> Blockquote
> Blockquote

And **bold**, *italics*. [A link](https://markdowntohtml.com) to somewhere.

And code highlighting:

```
var foo = 'bar';
function baz(s) {
   return foo + ':' + s;
}
```

Or inline code like `var foo = 'bar';`.

Or an image of bears

![bears](http://placebear.com/200/200)

The end ..."""
        htmlnode = md_to_htmlnode(markdown)
        expected_htmlnode = HTMLNode(tag="div", children=[[
            HTMLNode(tag="h1", children=[[HTMLNode(value="Sample Markdown")]]),
            HTMLNode(tag="p", children=[
                     [HTMLNode(value="This is some basic, sample markdown.")]]),
            HTMLNode(tag="h2", children=[[HTMLNode(value="Second Heading")]]),
            HTMLNode(tag="h3", children=[
                     [HTMLNode(value="Unordered lists:")]]),
            HTMLNode(tag="ul", children=[
                [HTMLNode(value="One")],
                [HTMLNode(value="Two")],
                [HTMLNode(value="Three")]]),
            HTMLNode(tag="h3", children=[[HTMLNode(value="Ordered lists:")]]),
            HTMLNode(tag="ol", children=[
                [HTMLNode(value="One")],
                [HTMLNode(value="Two")],
                [HTMLNode(value="Three")]]),
            HTMLNode(tag="blockquote", children=[
                     [HTMLNode(value="Blockquote")],
                     [HTMLNode(value="Blockquote")],
                     [HTMLNode(value="Blockquote")]]),
            HTMLNode(tag="p", children=[
                     [HTMLNode(value="And "),
                      HTMLNode(tag="b", value="bold"),
                      HTMLNode(value=", "),
                      HTMLNode(tag="i", value="italics"),
                      HTMLNode(value=". "),
                      HTMLNode(tag="a", value="A link", props={
                               "href": "https://markdowntohtml.com"}),
                      HTMLNode(value=" to somewhere.")]]),
            HTMLNode(tag="p", children=[
                [HTMLNode(value="And code highlighting:")]]),
            HTMLNode(tag="code", children=[
                     [HTMLNode(value="""var foo = 'bar';
function baz(s) {
   return foo + ':' + s;
}""")]]),
            HTMLNode(tag="p", children=[
                     [HTMLNode(value="Or inline code like "),
                      HTMLNode(tag="code", value="var foo = 'bar';"),
                      HTMLNode(value=".")]]),
            HTMLNode(tag="p", children=[
                     [HTMLNode(value="Or an image of bears")]]),
            HTMLNode(tag="p", children=[
                     [HTMLNode(tag="img", value="", props={
                               "src": "http://placebear.com/200/200", "alt": "bears"})]]),
            HTMLNode(tag="p", children=[[HTMLNode(value="The end ...")]]),
        ]])
        self.assertEqual(htmlnode, expected_htmlnode)


if __name__ == "__main__":
    unittest.main()
