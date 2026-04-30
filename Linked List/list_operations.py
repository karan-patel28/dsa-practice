from list_node import ListNode

def build_list(arr):
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()