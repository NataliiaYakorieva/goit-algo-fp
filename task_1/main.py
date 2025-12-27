from linked_list import LinkedList
from utils import merge_two_sorted_lists

if __name__ == "__main__":
    # Create and fill two lists
    ll1 = LinkedList()
    ll2 = LinkedList()
    for value in [1, 3, 5]:
        ll1.append(value)
    for value in [2, 4, 6]:
        ll2.append(value)

    print("List 1:")
    ll1.print_list()
    print("List 2:")
    ll2.print_list()

    # Reverse
    ll1.reverse()
    print("Reversed List 1:")
    ll1.print_list()

    # Sort
    ll1.sort()
    print("Sorted List 1:")
    ll1.print_list()

    # Merge
    merged_head = merge_two_sorted_lists(ll1.head, ll2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("Merged Sorted List:")
    merged_list.print_list()
