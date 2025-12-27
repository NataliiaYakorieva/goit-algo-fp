from typing import Optional


class Node:
    """
    Node of a singly linked list.

    Attributes:
        data (int): The value stored in the node.
        next (Optional[Node]): Reference to the next node in the list.
    """

    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional['Node'] = None
