from typing import List

class Solution:
    def reverse_list(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverse_list(nums, 0, len(nums) - 1)
        self.reverse_list(nums, k, len(nums) - 1)
        self.reverse_list(nums, 0, k - 1)
        

if __name__ == "__main__":
    obj = Solution()

    # Example 1
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    obj.rotate(nums1, k1)
    print(nums1)  # Expected: [5,6,7,1,2,3,4]

    # Example 2
    nums2 = [-1,-100,3,99]
    k2 = 2
    obj.rotate(nums2, k2)
    print(nums2)  # Expected: [3,99,-1,-100]