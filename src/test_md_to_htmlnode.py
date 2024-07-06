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

    def test_md_to_htmlnode2(self):
        md = """# Heading1

## Heading2

### Heading3

#### Heading4

##### Heading5

###### Heading6

Just text

**bold** *italic* `code`

1. **bold**
2. *italic*
3. `code`

* **bold**
* *italic*
* `code`

```
fn main(){
    fmt.Print("Hello world")
}
```

> Some quote
> Some quote
> Some quote

[bears](http://placebear.com/200/200)

![bears](http://placebear.com/200/200)"""
        html = md_to_htmlnode(md).to_html()

        expected_html = """<div><h1>Heading1</h1><h2>Heading2</h2><h3>Heading3</h3><h4>Heading4</h4><h5>Heading5</h5><h6>Heading6</h6><p>Just text</p><p><b>bold</b> <i>italic</i> <code>code</code></p><ol><li><b>bold</b></li><li><i>italic</i></li><li><code>code</code></li></ol><ul><li><b>bold</b></li><li><i>italic</i></li><li><code>code</code></li></ul><code>fn main(){
    fmt.Print("Hello world")
}</code><blockquote>Some quoteSome quoteSome quote</blockquote><p><a href="http://placebear.com/200/200">bears</a></p><p><img src="http://placebear.com/200/200" alt="bears"></p></div>"""

        self.assertEqual(html, expected_html)

if __name__ == "__main__":
    unittest.main()
