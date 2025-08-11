import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("p", "Hello", [], {"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    def test_repr(self):
        node = HTMLNode("a", "Link", None, {"href": "http://a.com"})
        self.assertEqual(
            repr(node),
            "HTMLNode(a, Link, None, {'href': 'http://a.com'})"
        )

    def test_props_to_html_none(self):
        node = HTMLNode("div", "Test", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty(self):
        node = HTMLNode("div", "Test", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode("div", "Test", None, {"id": "main"})
        self.assertEqual(node.props_to_html(), ' id="main"')

    def test_to_html_not_implemented(self):
        node = HTMLNode("div", "Test")
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()