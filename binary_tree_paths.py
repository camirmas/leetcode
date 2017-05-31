def binary_tree_paths(root_node):
    total = []
    nodes = [(root_node, [root_node.value])]

    while nodes:
        node, path = nodes.pop()

        if not node.left and not node.right:
            total.append(path)

        if node.left:
            l_path = path + [node.left.value]
            nodes.append((node.left, l_path))

        if node.right:
            r_path = path + [node.right.value]
            nodes.append((node.right, r_path))

    return total
