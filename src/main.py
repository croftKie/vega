from textnode import TextNode
from htmlnode import HtmlNode
from leafnode import LeafNode
def main():
    tn = TextNode("This is a text node", "bold", "https://www.boot.dev")
    hn = LeafNode(value="click me", tag="a", props={"href": "https://www.google.com", "target": "_blank"})

    print(hn.to_html())
main()