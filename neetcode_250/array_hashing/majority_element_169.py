from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        half = len(nums) / 2

        for i in nums:
            res[i] = res.get(i,0) + 1
            if res[i] > half:
                return i

        return -1

if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([6, 5, 5], 5),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.majorityElement(nums)
        passed = result == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: majorityElement({nums}) -> {result} (expected {expected}) [{status}]")