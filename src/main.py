from copy_dir import copy_dir
from generate_page import generate_pages

static_dir_path = "./static"
content_dir_path = "./content"
template_path = "./template.html"
public_dir_path = "./public"


def main():
    copy_dir(static_dir_path, public_dir_path)
    generate_pages(content_dir_path, template_path, public_dir_path)


main()
