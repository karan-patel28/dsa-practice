from typing import Optional
from list_node import ListNode
import list_operations as lo

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

    # Example 1
    head1 = lo.build_list([1,2,3,4,5])
    result1 = obj.reverseList(head1)
    lo.print_list(result1)  # Expected: 5 -> 4 -> 3 -> 2 -> 1

    # Example 2
    head2 = lo.build_list([1,2])
    result2 = obj.reverseList(head2)
    lo.print_list(result2)  # Expected: 2 -> 1

    # Example 3
    head3 = lo.build_list([])
    result3 = obj.reverseList(head3)
    lo.print_list(result3)  # Expected: (empty)