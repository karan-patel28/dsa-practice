from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(currSum, maxSum)

        return maxSum / k


if __name__ == "__main__":
    obj = Solution()

    # Example 1
    nums1 = [1,12,-5,-6,50,3]
    k1 = 4
    result1 = obj.findMaxAverage(nums1, k1)
    print(result1)  # Expected: 12.75

    # Example 2
    nums2 = [5]
    k2 = 1
    result2 = obj.findMaxAverage(nums2, k2)
    print(result2)  # Expected: 5.0