import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("span", "Highlight", {"class": "highlight", "id": "h1"})
        # Order of props in string may vary depending on Python version
        html = node.to_html()
        self.assertTrue(html.startswith('<span'))
        self.assertIn('class="highlight"', html)
        self.assertIn('id="h1"', html)
        self.assertTrue(html.endswith('>Highlight</span>'))

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_empty_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_none_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("span", "one")
        child2 = LeafNode("span", "two")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><span>one</span><span>two</span></div>")

    def test_to_html_with_props(self):
        child = LeafNode("span", "child")
        parent_node = ParentNode("div", [child], {"class": "container", "id": "main"})
        html = parent_node.to_html()
        self.assertTrue(html.startswith('<div'))
        self.assertIn('class="container"', html)
        self.assertIn('id="main"', html)
        self.assertTrue(html.endswith('</div>'))

    def test_to_html_missing_tag(self):
        child = LeafNode("span", "child")
        parent_node = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_missing_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_empty_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_child_raises(self):
        bad_child = LeafNode("p", None)
        parent_node = ParentNode("div", [bad_child])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_nested_empty_parent(self):
        empty_parent = ParentNode("span", [])
        parent_node = ParentNode("div", [empty_parent])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_repr(self):
        children = [LeafNode("span", "child")]
        parent_node = ParentNode("div", children, {"class": "container"})
        self.assertEqual(
            repr(parent_node),
            f"HTMLNode(div, None, {children}, {{'class': 'container'}})"
        )
if __name__ == "__main__":
    unittest.main()