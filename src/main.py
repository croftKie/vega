from inline_markdown import extract_markdown_images
from block_markdown import markdown_to_blocks
def main():
    # tn = extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)")

    # print(tn)

    md = """    This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""

    # markdown_to_blocks(md)
    print(markdown_to_blocks(md))

main()