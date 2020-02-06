class Node:
    def __init__(self, left: "Node", right: "Node", text: str):
        self.left = left
        self.right = right
        self.text = text

    def __str__(self):
        return str(self.left) + str(self.right)


def create_hoffman_tree(queue):
    while True:
        queue.sort(key=lambda t: t[1])
        if len(queue) > 1:
            left, right = queue.pop(0), queue.pop(0)
            node = Node(left[0], right[0], str(left[0]) + str(right[0]))
            queue.append((node, left[1] + right[1]))
        else:
            return queue[0][0]


def encode_text(text: str, tree: Node):
    output = []
    for c in text:
        encoded_letter = ""
        node = tree
        while True:
            try:
                if c in str(node.left):
                    encoded_letter += "0"
                    node = node.left
                else:
                    encoded_letter += "1"
                    node = node.right
            except AttributeError:
                break
        output.append(encoded_letter)
    return "".join(output)


def decode_text(encoded: str, tree: Node):
    output = ""
    node = tree
    for c in encoded:
        if c == "0":
            node = node.left
        else:
            node = node.right
        try:
            output += node
            node = tree
        except TypeError:
            pass
    return output
