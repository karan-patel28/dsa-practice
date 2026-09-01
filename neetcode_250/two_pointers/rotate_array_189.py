from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverse_array(nums, 0, len(nums) - 1)
        self.reverse_array(nums, k, len(nums) - 1)
        self.reverse_array(nums, 0, k - 1)

    def reverse_array(self, nums, left, right):
        while left < right:
            nums[left],nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2], 3, [2, 1]),
        ([1], 0, [1]),
        ([1, 2, 3], 0, [1, 2, 3]),
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        nums_copy = nums.copy()
        sol.rotate(nums_copy, k)
        passed = nums_copy == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: rotate({nums}, {k}) -> {nums_copy} (expected {expected}) [{status}]")