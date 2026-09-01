from typing import List
from collections import Counter


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0

        for i in nums:
            if i != val:
                nums[idx] = i
                idx += 1

        return idx



if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([1], 1, 0, []),
        ([4, 5], 4, 1, [5]),
    ]

    for i, (nums, val, expected_k, expected_remaining) in enumerate(test_cases, 1):
        nums_copy = nums.copy()
        k = sol.removeElement(nums_copy, val)
        # order of the first k elements doesn't matter, so compare as multisets
        remaining_correct = Counter(nums_copy[:k]) == Counter(expected_remaining)
        passed = k == expected_k and remaining_correct
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: removeElement({nums}, {val}) -> k={k}, nums={nums_copy[:k]} (expected k={expected_k}, elements={expected_remaining}) [{status}]")