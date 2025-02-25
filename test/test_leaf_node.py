import unittest
from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_valid_tag_and_value(self):
        node = LeafNode(tag="span", value="Hello", props={"class": "example"})
        expected = '<span class="example">Hello</span>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_empty_tag(self):
        node = LeafNode(tag="", value="Hello")
        expected = "Hello"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_none_tag(self):
        node = LeafNode(tag=None, value="Hello")
        expected = "Hello"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_raises_value_error_for_none_value(self):
        node = LeafNode(tag="div", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_raises_value_error_for_empty_value(self):
        node = LeafNode(tag="div", value="")
        with self.assertRaises(ValueError):
            node.to_html()