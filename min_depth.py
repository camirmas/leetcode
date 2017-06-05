def min_depth(root):
    if not root:
        return 0

    nodes = []
    nodes.append((root, 1))
    min_depth = float('inf')

    while nodes:
        node, depth = nodes.pop()

        if not node.left and not node.right:
            min_depth = min(min_depth, depth)

        if node.left:
            nodes.append((node.left, depth + 1))

        if node.right:
            nodes.append((node.right, depth + 1))

    return min_depth

