# test_textnode.py
import unittest

from textnode import TextNode, TextType


class Testtest(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equality(self):
        node1 = TextNode("Hello", TextType.NORMAL)
        node2 = TextNode("Hello", TextType.NORMAL)
        self.assertEqual(node1, node2)

    def test_inequality_different_text(self):
        node1 = TextNode("Hello", TextType.NORMAL)
        node2 = TextNode("World", TextType.NORMAL)
        self.assertNotEqual(node1, node2)

    def test_inequality_different_text_type(self):
        node1 = TextNode("Hello", TextType.NORMAL)
        node2 = TextNode("Hello", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_inequality_different_url(self):
        node1 = TextNode("Hello", TextType.LINK, "http://example.com")
        node2 = TextNode("Hello", TextType.LINK, "http://example.org")
        self.assertNotEqual(node1, node2)

    def test_none_comparison(self):
        node = TextNode("Hello", TextType.NORMAL)
        self.assertNotEqual(node, None)

    def test_different_object_comparison(self):
        node = TextNode("Hello", TextType.NORMAL)
        self.assertNotEqual(node, 123)

    def test_empty_text(self):
        node1 = TextNode("", TextType.NORMAL)
        node2 = TextNode("", TextType.NORMAL)
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Hello", TextType.NORMAL)
        self.assertEqual(repr(node), "TextNode(Hello, TextType.NORMAL, None)")

    def test_with_url(self):
        node = TextNode("Hello", TextType.LINK, "http://example.com")
        self.assertEqual(node.url, "http://example.com")


if __name__ == "__main__":
    unittest.main()
