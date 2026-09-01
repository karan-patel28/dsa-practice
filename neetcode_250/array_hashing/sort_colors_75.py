from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0

        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            else:
                two += 1

        idx = 0

        while idx < len(nums):
            if zero > 0:
                nums[idx] = 0
                zero -= 1
            elif one > 0:
                nums[idx] = 1
                one -= 1
            else:
                nums[idx] = 2
                two -= 1
            idx += 1


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([1, 2, 0], [0, 1, 2]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        nums_copy = nums.copy()
        sol.sortColors(nums_copy)
        passed = nums_copy == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: sortColors({nums}) -> {nums_copy} (expected {expected}) [{status}]")