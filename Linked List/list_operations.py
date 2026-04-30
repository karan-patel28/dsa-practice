from list_node import ListNode

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

def build_list(arr):
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

def build_list(arr, pos):
        dummy = ListNode(0)
        curr = dummy
        cycle_node = None

        for i, val in enumerate(arr):
            curr.next = ListNode(val)
            curr = curr.next
            if i == pos:
                cycle_node = curr

        if pos != -1:
            curr.next = cycle_node  # create cycle

        return dummy.next