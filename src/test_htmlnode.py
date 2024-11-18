import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    # HTMLNode
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "hero", "href": "google.com"})
        self.assertEqual(node.props_to_html(),' class="hero" href="google.com"')

    def test_values(self):
        node = HTMLNode("div", "This is a value")

        self.assertEqual(node.tag, "div")

        self.assertEqual(node.value, "This is a value")

        self.assertEqual(node.children, None)

        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("div", "The div is surely centered", None, {"class": "center"})

        self.assertEqual(node.__repr__(), "HTMLNode(div, The div is surely centered, children: None, {'class': 'center'})")

    # LeaNode
    def test_to_html_no_children(self):
        node = LeafNode("p", "This is the value.")

        self.assertEqual(node.to_html(), "<p>This is the value.</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "No tags just raw text.")

        self.assertEqual(node.to_html(), "No tags just raw text.")

    def test_repr_LeafNode(self):
        node = LeafNode("div", "The div is surely centered", {"class": "center"})

        self.assertEqual(node.__repr__(), "LeafNode(div, The div is surely centered, {'class': 'center'})")


if __name__ == "__main__":
    unittest.main()