import unittest

from src.block_markdown import markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_boot_dev_case(self):
        md_text = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        self.assertEqual(
            [
                '# This is a heading',
                'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
                '- This is the first list item in a list block\n- This is a list item\n- This is another list item'
            ],
            markdown_to_blocks(md_text),
        )

    def test_boot_dev_case_with_whitespace(self):
        md_text = """  # This is a heading  

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.


  - This is the first list item in a list block
- This is a list item
- This is another list item   """
        self.assertEqual(
            [
                '# This is a heading',
                'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
                '- This is the first list item in a list block\n- This is a list item\n- This is another list item'
            ],
            markdown_to_blocks(md_text),
        )

    def test_empty_string_returns_empty_list(self):
        self.assertEqual([], markdown_to_blocks(""))

    def test_single_newline_keeps_text_in_same_block(self):
        md_text = "This is line 1\nThis is line 2"
        self.assertEqual(
            ["This is line 1\nThis is line 2"],
            markdown_to_blocks(md_text)
        )

    def test_multiple_paragraphs_with_triple_newlines(self):
        md_text = "Paragraph 1\n\n\nParagraph 2\n\n\nParagraph 3"
        self.assertEqual(
            ["Paragraph 1", "Paragraph 2", "Paragraph 3"],
            markdown_to_blocks(md_text)
        )

    def test_blocks_with_trailing_whitespace(self):
        md_text = "Block 1  \n\nBlock 2  "
        self.assertEqual(
            ["Block 1", "Block 2"],
            markdown_to_blocks(md_text)
        )

    def test_single_character_blocks(self):
        md_text = "a\n\nb\n\nc"
        self.assertEqual(
            ["a", "b", "c"],
            markdown_to_blocks(md_text)
        )

    def test_blocks_with_special_characters(self):
        md_text = "#Header\n\n*List\n-item\n\n>Quote"
        self.assertEqual(
            ["#Header", "*List\n-item", ">Quote"],
            markdown_to_blocks(md_text)
        )
