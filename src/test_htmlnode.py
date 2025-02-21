import unittest
from htmlnode import HTMLNode

class TestHTMLNodeBehavior(unittest.TestCase):
    def test_repr_includes_all_attributes(self):
        node = HTMLNode(tag="div", value="Hello", children=["child"], props={"class": "example"})
        expected = "HTMLNode(div, Hello, ['child'], {'class': 'example'})"
        self.assertEqual(repr(node), expected)

    def test_repr_with_default_values(self):
        node = HTMLNode()
        expected = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(node), expected)

    def test_to_html_raises_not_implemented_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()