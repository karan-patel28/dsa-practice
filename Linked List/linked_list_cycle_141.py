from typing import Optional
from list_node import ListNode
import list_operations as lo

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    
if __name__ == "__main__":
    obj = Solution()

    # Example 1: cycle at index 1
    head1 = lo.build_list_cycle([3,2,0,-4], 1)
    print(obj.hasCycle(head1))  # Expected: True

    # Example 2: cycle at index 0
    head2 = lo.build_list_cycle([1,2], 0)
    print(obj.hasCycle(head2))  # Expected: True

    # Example 3: no cycle
    head3 = lo.build_list_cycle([1], -1)
    print(obj.hasCycle(head3))  # Expected: False