from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)
import re

def split_nodes_with_delimiter(input_nodes, delimiter, text_type):
    new_node_list = []
    for input_node in input_nodes:
        if input_node.text_type != text_type_text:
            new_node_list.append(input_node)
            continue
        divided_inline_nodes = []
        text_sections = input_node.text.split(delimiter)
        if len(text_sections) % 2 == 0:
            raise ValueError("Invalid Markdown: Formatted secction not closed as expected")
        for i in range(len(text_sections)):
            if text_sections[i] == "":
                continue
            if i % 2 == 0:
                divided_inline_nodes.append(TextNode(text_sections[i], text_type_text))
            else:
                divided_inline_nodes.append(TextNode(text_sections[i], text_type))
        new_node_list.extend(divided_inline_nodes)
    return new_node_list

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    extract = re.findall(regex, text)
    return extract

def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"
    extract = re.findall(regex, text)
    return extract

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type=text_type_text)]
    nodes = split_nodes_with_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_with_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_with_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes