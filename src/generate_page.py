import os
from md_to_htmlnode import *


def generate_pages(src: os.path, tmpl: os.path, dst: os.path):
    if os.path.isfile(src):
        generate_page(src, tmpl, dst.replace(".md", ".html"))
        return

    for src_entrie in os.listdir(src):
        generate_pages(os.path.join(src, src_entrie),
                       tmpl,
                       os.path.join(dst, src_entrie))


def generate_page(src: os.path, tmpl: os.path, dst: os.path):
    with open(src) as src_file:
        md = src_file.read()
    with open(tmpl) as tmpl_file:
        html_tmpl = tmpl_file.read()

    content = md_to_htmlnode(md).to_html()
    title = extract_title(md)
    html = html_tmpl.replace(
        "{{ Title }}", title).replace(
        "{{ Content }}", content)

    dest_dir_path = os.path.dirname(dst)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dst, "w") as dst_file:
        dst_file.write(html)


def extract_title(md: str) -> str:
    for line in md.split("\n"):
        line = line.strip()
        if line[:2] == "# ":
            return line[2:]
    raise Exception("Cant find h1 header in:", md)
