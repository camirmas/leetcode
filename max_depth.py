def max_depth(root):
    if not root:
        return 0

    nodes = []
    nodes.append((root, 1))
    max_depth = 1

    while nodes:
        node, depth = nodes.pop()

        if not node.left and not node.right:
            max_depth = max(max_depth, depth)

        if node.left:
            nodes.append((node.left, depth + 1))

        if node.right:
            nodes.append((node.right, depth + 1))

    return max_depth
