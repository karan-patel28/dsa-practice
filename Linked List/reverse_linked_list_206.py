from typing import Optional
from ListNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
    
if __name__ == "__main__":
    obj = Solution()

    # Helper to create linked list
    def build_list(arr):
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    # Helper to print linked list
    def print_list(head):
        curr = head
        while curr:
            print(curr.val, end=" -> " if curr.next else "")
            curr = curr.next
        print()

    # Example 1
    head1 = build_list([1,2,3,4,5])
    result1 = obj.reverseList(head1)
    print_list(result1)  # Expected: 5 -> 4 -> 3 -> 2 -> 1

    # Example 2
    head2 = build_list([1,2])
    result2 = obj.reverseList(head2)
    print_list(result2)  # Expected: 2 -> 1

    # Example 3
    head3 = build_list([])
    result3 = obj.reverseList(head3)
    print_list(result3)  # Expected: (empty)