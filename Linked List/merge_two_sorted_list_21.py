from typing import Optional
from list_node import ListNode
import list_operations as lo

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return head.next
    
if __name__ == "__main__":
    obj = Solution()

    list1 = lo.build_list([1, 2, 4])
    list2 = lo.build_list([1, 3, 4])

    result = obj.mergeTwoLists(list1, list2)
    lo.print_list(result)  # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4