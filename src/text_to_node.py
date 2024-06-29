import re
from textnode import *


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = list[TextNode]()
    for old_node in old_nodes:
        if type(old_node) is not TextNode:
            new_nodes.append(old_node)

        splited_text = old_node.text.split(delimiter)
        text_types = [old_node.text_type, text_type]

        if len(splited_text) % 2 != 1:
            raise Exception("matching closing delimeter is not found")
        for switcher in range(len(splited_text)):
            if not splited_text[switcher]:
                continue

            new_node = TextNode(
                splited_text[switcher], text_types[switcher % 2])
            new_nodes.append(new_node)

    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = list[TextNode]()
    for old_node in old_nodes:
        if type(old_node) is not TextNode:
            new_nodes.append(old_node)

        extracted_images = extract_markdown_images(old_node.text)
        text_to_split = old_node.text

        for (alt, src) in extracted_images:
            splited_text = text_to_split.split(
                f"![{alt}]({src})", 1)

            text_before_image = splited_text[0]
            if text_before_image != "":
                new_nodes.append(
                    TextNode(text_before_image, old_node.text_type))
            new_nodes.append(TextNode(alt, TextType.IMAGE, src))

            text_to_split = splited_text[1]

        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, old_node.text_type))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = list[TextNode]()
    for old_node in old_nodes:
        if type(old_node) is not TextNode:
            new_nodes.append(old_node)

        extracted_links = extract_markdown_links(old_node.text)
        text_to_split = old_node.text

        for (alt, src) in extracted_links:
            splited_text = text_to_split.split(
                f"[{alt}]({src})", 1)

            text_before_link = splited_text[0]
            if text_before_link != "":
                new_nodes.append(
                    TextNode(text_before_link, old_node.text_type))
            new_nodes.append(TextNode(alt, TextType.LINK, src))

            text_to_split = splited_text[1]

        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, old_node.text_type))

    return new_nodes
