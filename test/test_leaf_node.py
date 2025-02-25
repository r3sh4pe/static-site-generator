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

    def test_repr_with_tag_value_props(self):
        node = LeafNode("div", "content", {"class": "test"})
        self.assertEqual(repr(node), "LeafNode(div, content, {'class': 'test'})")

    def test_repr_with_tag_value_no_props(self):
        node = LeafNode("span", "text")
        self.assertEqual(repr(node), "LeafNode(span, text, None)")

    def test_repr_with_empty_tag(self):
        node = LeafNode("", "content")
        self.assertEqual(repr(node), "LeafNode(, content, None)")

    def test_repr_with_none_tag(self):
        node = LeafNode(None, "content")
        self.assertEqual(repr(node), "LeafNode(None, content, None)")

    def test_repr_with_empty_value(self):
        node = LeafNode("div", "")
        self.assertEqual(repr(node), "LeafNode(div, , None)")

    def test_repr_with_none_value(self):
        node = LeafNode("div", None)
        self.assertEqual(repr(node), "LeafNode(div, None, None)")
