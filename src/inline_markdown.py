from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        split_nodes = node.text.split(delimiter)
        nodes = []

        if len(split_nodes) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        for i in range(len(split_nodes)):
            if split_nodes[i] == "":
                continue
            elif i % 2 == 0:
                nodes.append(TextNode(split_nodes[i], node.text_type))
            else:
                nodes.append(TextNode(split_nodes[i], text_type))

    new_nodes.extend(nodes)
    
    return new_nodes