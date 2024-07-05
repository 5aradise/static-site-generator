from md_to_htmlnode import *


def main():
    markdown = """# h1 Heading

## h2 Heading

### h3 Heading

#### h4 Heading

##### h5 Heading

###### h6 Heading

**This is bold text**

*This is italic text*

## Lists

Unordered

* Create a list by starting a line with `-`
* Sub-lists are made by indenting 2 spaces:
* Marker character change forces new list start:
* Ac tristique libero volutpat at
* Facilisis in pretium nisl aliquet
* Nulla volutpat aliquam velit
* Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

## Code

```
Sample text here...
```
"""
    html_node = md_to_htmlnode(markdown)
    print(html_node.to_html())


main()
