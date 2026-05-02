from typing import Optional
from list_node import ListNode
import list_operations as lo

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return curr

if __name__ == "__main__":
    obj = Solution()

    # Example 1
    head1 = lo.build_list([1,1,2])
    result1 = obj.deleteDuplicates(head1)
    lo.print_list(result1)  # Expected: 1 -> 2

    # Example 2
    head2 = lo.build_list([1,1,2,3,3])
    result2 = obj.deleteDuplicates(head2)
    lo.print_list(result2)  # Expected: 1 -> 2 -> 3