import re

def markdown_to_blocks(md):
    blocks = []
    regex = r"[ ]{2,}|[	]"
    
    ws = re.findall(regex, md)

    for block in md.split("\n"):
        stripped = re.sub(regex, "", block)
        if(stripped != ""):
            blocks.append(stripped)

    return blocks

    pass