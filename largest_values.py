def largest_values(root):
    """Finds the largest value in each row of a binary tree."""
    maxes = []

    if not root:
        return maxes

    nodes = [(root, 0)]

    while nodes:
        node, depth = nodes.pop(0)

        if len(maxes) <= depth:
            maxes.append(node.val)
        elif node.val > maxes[depth]:
            maxes[depth] = node.val

        if node.left:
            nodes.append((node.left, depth + 1))

        if node.right:
            nodes.append((node.right, depth + 1))

    return maxes
