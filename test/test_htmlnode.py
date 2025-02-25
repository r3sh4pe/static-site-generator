import unittest

from src.htmlnode import HTMLNode


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

    def test_repr_with_empty_children_list(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "example"})
        expected = "HTMLNode(div, Hello, [], {'class': 'example'})"
        self.assertEqual(repr(node), expected)

    def test_repr_with_none_children(self):
        node = HTMLNode(tag="div", value="Hello", children=None, props={"class": "example"})
        expected = "HTMLNode(div, Hello, None, {'class': 'example'})"
        self.assertEqual(repr(node), expected)

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(props={"class": "example", "id": "main"})
        expected = ' class="example" id="main"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_with_empty_props(self):
        node = HTMLNode(props={})
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_with_none_props(self):
        node = HTMLNode(props=None)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
