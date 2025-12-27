from collections import deque
from typing import List, Optional
from task_4 import Node, draw_tree


def generate_colors(n: int) -> List[str]:
    """
    Generate a list of color hex strings with blue gradient.

    Args:
        n (int): Number of colors to generate.

    Returns:
        List[str]: List of color hex strings.
    """
    colors: List[str] = []
    for i in range(n):
        # Calculate intensity for gradient effect
        intensity = int(255 - (255 * i / (n - 1))) if n > 1 else 255
        color = f"#{intensity:02x}{intensity:02x}{255:02x}"
        colors.append(color)
    return colors


def dfs_traversal(root: Optional[Node]) -> List[Node]:
    """
    Perform depth-first search (DFS) traversal of a binary tree.

    Args:
        root (Optional[Node]): The root node of the tree.

    Returns:
        List[Node]: List of nodes in DFS order.
    """
    if not root:
        return []

    visited: List[Node] = []
    stack: List[Node] = [root]

    while stack:
        node = stack.pop()
        visited.append(node)

        # Push right child first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def bfs_traversal(root: Optional[Node]) -> List[Node]:
    """
    Perform breadth-first search (BFS) traversal of a binary tree.

    Args:
        root (Optional[Node]): The root node of the tree.

    Returns:
        List[Node]: List of nodes in BFS order.
    """
    if not root:
        return []

    visited: List[Node] = []
    queue: deque[Node] = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


if __name__ == "__main__":
    # Tree construction
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Depth-first traversal and coloring
    dfs_order = dfs_traversal(root)
    colors = generate_colors(len(dfs_order))
    for i, node in enumerate(dfs_order):
        node.color = colors[i]

    draw_tree(root)

    # Breadth-first traversal and coloring
    bfs_order = bfs_traversal(root)
    colors = generate_colors(len(bfs_order))
    for i, node in enumerate(bfs_order):
        node.color = colors[i]

    draw_tree(root)
