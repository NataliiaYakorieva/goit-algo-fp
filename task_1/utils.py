from typing import Optional
from node import Node


def get_middle(head: Node) -> Node:
    """
    Find the middle node of the linked list.

    Args:
        head (Node): Head node of the list.

    Returns:
        Node: Middle node.
    """
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_two_sorted_lists(
        l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    """
    Merge two sorted singly linked lists into one sorted list.

    Args:
        l1 (Optional[Node]): Head of the first sorted list.
        l2 (Optional[Node]): Head of the second sorted list.

    Returns:
        Optional[Node]: Head of the merged sorted list.
    """
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next
