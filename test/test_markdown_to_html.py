import unittest

from src.markdown_blocks import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here\nThis is the same paragraph on a new line</p></div>"
        )

    def test_headings(self):
        md = """
# Heading 1

## Heading 2 with **bold**

### Heading 3
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2 with <b>bold</b></h2><h3>Heading 3</h3></div>"
        )

    def test_lists(self):
        md = """
- Item 1
- Item 2
- Item 3 with **bold**

1. First item
2. Second item with _italic_
3. Third item
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3 with <b>bold</b></li></ul><ol><li>First item</li><li>Second item with <i>italic</i></li><li>Third item</li></ol></div>"
        )

    def test_code_blocks(self):
        md = """
```
def hello_world():
    print("Hello, world!")
```
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><pre><code>def hello_world():\n    print(\"Hello, world!\")</code></pre></div>"
        )

    def test_quotes(self):
        md = """
> This is a quote
> with multiple lines
> and **bold** text
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines and <b>bold</b> text</blockquote></div>"
        )

    def test_mixed_content(self):
        md = """
# Markdown Parser

This is a **markdown** parser that converts _markdown_ to HTML.

## Features

- Paragraphs
- **Bold** text
- _Italic_ text
- `Code` blocks
- [Links](https://example.com)
- Images: ![alt text](https://example.com/image.png)

## Code Example

```
def example():
    return "This is an example"
```

> This is a blockquote
> with multiple lines
"""
        html = markdown_to_html_node(md).to_html()
        # Check for key elements instead of comparing the full string
        self.assertIn("<h1>Markdown Parser</h1>", html)
        self.assertIn("<p>This is a <b>markdown</b> parser that converts <i>markdown</i> to HTML.</p>", html)
        self.assertIn("<h2>Features</h2>", html)
        self.assertIn("<ul>", html)
        self.assertIn("<li>Paragraphs</li>", html)
        self.assertIn("<li><b>Bold</b> text</li>", html)
        self.assertIn("<pre><code>", html)
        self.assertIn("<blockquote>", html)


if __name__ == "__main__":
    unittest.main()