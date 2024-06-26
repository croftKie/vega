from textnode import text_type_text, text_type_bold, text_type_code, text_type_italic, TextNode

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
