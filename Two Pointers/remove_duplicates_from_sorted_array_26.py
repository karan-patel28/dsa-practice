from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(len(nums)):
            print(nums[right])
        return nums

if __name__ == "__main__":
    obj = Solution()

    # Example 1
    nums1 = [1, 1, 2]
    k1 = obj.removeDuplicates(nums1)
    print(k1)

    # Example 2
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = obj.removeDuplicates(nums2)
    print(k2)