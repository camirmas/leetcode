def level_order_traversal(root):
    if not root:
        return []

    nodes = []
    nodes.append((root, 1))
    rows = []

    while nodes:
        node, depth = nodes.pop(0)

        if len(rows) < depth:
            rows.append([node.val])
        else:
            rows[depth - 1].append(node.val)

        if node.left:
            nodes.append((node.left, depth + 1))

        if node.right:
            nodes.append((node.right, depth + 1))

    return rows
