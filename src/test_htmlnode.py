import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
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
    


if __name__ == "__main__":
    unittest.main()