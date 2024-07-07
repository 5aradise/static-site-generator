from generate_page import generate_page


content_path = "content/index.md"
template_path = "template.html"
public_path = "public/index.html"


def main():
    generate_page(content_path, template_path, public_path)


main()
