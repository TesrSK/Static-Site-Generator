import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
    
    # ParentNode
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_many_children(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])

        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",)
    
    def test_headings(self):
        node = ParentNode("h2", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        
        self.assertEqual(node.to_html(), "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>")

if __name__ == "__main__":
    unittest.main()