from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        one_count = 0
        two_count = 0
        idx = 0

        for i in nums:
            if i == 0:
                zero_count += 1
            elif i == 1:
                one_count += 1
            else:
                two_count += 1

        while idx < len(nums):
            if zero_count > 0:
                nums[idx] = 0
                zero_count -= 1
            elif one_count > 0:
                nums[idx] = 1
                one_count -= 1
            elif two_count > 0:
                nums[idx] = 2
                two_count -= 1
            
            idx += 1

if __name__ == "__main__":
    obj = Solution()

    # Example 1
    nums1 = [2,0,2,1,1,0]
    obj.sortColors(nums1)
    print(nums1)  # Expected: [0,0,1,1,2,2]

    # Example 2
    nums2 = [2,0,1]
    obj.sortColors(nums2)
    print(nums2)  # Expected: [0,1,2]