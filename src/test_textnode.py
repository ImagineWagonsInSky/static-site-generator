import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq_text(self):
        node1 = TextNode("Text 1", TextType.BOLD)
        node2 = TextNode("Text 2", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_url(self):
        node1 = TextNode("Text", TextType.LINK, "http://a.com")
        node2 = TextNode("Text", TextType.LINK, "http://b.com")
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("Text", TextType.LINK, "http://a.com")
        node2 = TextNode("Text", TextType.LINK, "http://a.com")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Hello", TextType.TEXT, None)
        self.assertEqual(repr(node), "TextNode(Hello, text, None)")


if __name__ == "__main__":
    unittest.main()