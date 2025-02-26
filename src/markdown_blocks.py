from enum import Enum

from src.inline_markdown import text_to_textnodes
from src.textnode import text_node_to_html_node
from src.htmlnode import ParentNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            html_nodes.append(paragraph_to_html_node(block))
        elif block_type == BlockType.HEADING:
            html_nodes.append(heading_to_html_node(block))
        elif block_type == BlockType.CODE:
            html_nodes.append(code_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            html_nodes.append(quote_to_html_node(block))
        elif block_type == BlockType.ULIST:
            html_nodes.append(unordered_list_to_html_node(block))
        elif block_type == BlockType.OLIST:
            html_nodes.append(ordered_list_to_html_node(block))

    return ParentNode("div", html_nodes)


def paragraph_to_html_node(block):
    text_nodes = text_to_textnodes(block)

    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

    return ParentNode("p", html_nodes)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break

    content = block[level:].strip()

    text_nodes = text_to_textnodes(content)

    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

    return ParentNode(f"h{level}", html_nodes)


def code_to_html_node(block):
    lines = block.split("\n")
    code_content = "\n".join(lines[1:-1]) if len(lines) > 2 else ""

    from src.textnode import TextNode, TextType
    text_node = TextNode(code_content, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)

    code_node = ParentNode("code", [html_node])
    return ParentNode("pre", [code_node])


def quote_to_html_node(block):
    lines = block.split("\n")
    quote_content = " ".join([line[1:].strip() for line in lines])

    text_nodes = text_to_textnodes(quote_content)

    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

    return ParentNode("blockquote", html_nodes)


def unordered_list_to_html_node(block):
    lines = block.split("\n")

    list_items = []
    for line in lines:
        item_content = line[2:].strip()

        text_nodes = text_to_textnodes(item_content)

        html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

        list_items.append(ParentNode("li", html_nodes))

    return ParentNode("ul", list_items)


def ordered_list_to_html_node(block):
    lines = block.split("\n")

    list_items = []
    for line in lines:
        pos = line.find(". ") + 2
        item_content = line[pos:].strip()

        text_nodes = text_to_textnodes(item_content)

        html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

        list_items.append(ParentNode("li", html_nodes))

    return ParentNode("ol", list_items)