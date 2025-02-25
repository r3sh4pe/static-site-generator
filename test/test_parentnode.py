import unittest

from src.leafnode import LeafNode
from src.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_valid_tag_and_children(self):
        child1 = LeafNode(tag="span", value="Hello")
        child2 = LeafNode(tag="span", value="World")
        node = ParentNode(tag="div", children=[child1, child2], props={"class": "example"})
        expected = '<div class="example"><span>Hello</span><span>World</span></div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_empty_tag(self):
        child = LeafNode(tag="span", value="Hello")
        node = ParentNode(tag="", children=[child])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_none_tag(self):
        child = LeafNode(tag="span", value="Hello")
        node = ParentNode(tag=None, children=[child])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_empty_children(self):
        node = ParentNode(tag="div", children=[])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_none_children(self):
        node = ParentNode(tag="div", children=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_nested_children(self):
        child1 = LeafNode(tag="span", value="Hello")
        child2 = ParentNode(tag="div", children=[LeafNode(tag="span", value="World")])
        node = ParentNode(tag="div", children=[child1, child2])
        expected = '<div><span>Hello</span><div><span>World</span></div></div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_props_with_special_characters(self):
        child = LeafNode(tag="span", value="Hello")
        node = ParentNode(tag="div", children=[child], props={"class": "example", "data-info": "some & info"})
        expected = '<div class="example" data-info="some & info"><span>Hello</span></div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_mixed_children(self):
        child1 = LeafNode(tag="span", value="Hello")
        child2 = ParentNode(tag="div", children=[LeafNode(tag="span", value="World")])
        node = ParentNode(tag="section", children=[child1, child2])
        expected = '<section><span>Hello</span><div><span>World</span></div></section>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_props_with_none_values(self):
        child = LeafNode(tag="span", value="Hello")
        node = ParentNode(tag="div", children=[child], props={"class": None, "id": "main"})
        expected = '<div id="main"><span>Hello</span></div>'
        self.assertEqual(node.to_html(), expected)

    def test_repr_returns_correct_format(self):
        node = ParentNode(tag="div", children=[], props={"class": "container"})
        assert repr(node) == "ParenNode(div, [], {'class': 'container'})"

    def test_repr_handles_empty_props(self):
        node = ParentNode(tag="div", children=[])
        assert repr(node) == "ParenNode(div, [], None)"

    def test_repr_handles_none_tag(self):
        node = ParentNode(tag=None, children=[])
        assert repr(node) == "ParenNode(None, [], None)"
