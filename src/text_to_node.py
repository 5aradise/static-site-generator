import re
from textnode import *


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = list[TextType]()
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
