from typing import Optional
from node import Node
from utils import get_middle


class LinkedList:
    """
    Singly linked list implementation.
    """

    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: int) -> None:
        """
        Add a new node with the given data to the end of the list.

        Args:
            data (int): Value to add.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self) -> None:
        """
        Print all elements in the list.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        """
        Reverse the linked list in place.
        """
        prev: Optional[Node] = None
        current: Optional[Node] = self.head
        while current:
            next_node: Optional[Node] = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        """
        Sort the linked list using merge sort algorithm.

        Args:
            head (Optional[Node]): Head node of the list to sort.

        Returns:
            Optional[Node]: Head node of the sorted list.
        """
        if not head or not head.next:
            return head

        middle = get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def sorted_merge(self, a: Optional[Node],
                     b: Optional[Node]) -> Optional[Node]:
        """
        Merge two sorted linked lists.

        Args:
            a (Optional[Node]): Head of the first sorted list.
            b (Optional[Node]): Head of the second sorted list.

        Returns:
            Optional[Node]: Head of the merged sorted list.
        """
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def sort(self) -> None:
        """
        Sort the entire linked list.
        """
        self.head = self.merge_sort(self.head)
