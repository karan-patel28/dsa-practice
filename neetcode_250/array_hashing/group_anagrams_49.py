from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        print(strs)


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "bca", "cab", "xyz"], [["abc", "bca", "cab"], ["xyz"]]),
    ]

    def normalize(groups):
        # sort each inner group, then sort the outer list of groups
        return sorted(sorted(g) for g in groups) if groups is not None else None

    for i, (strs, expected) in enumerate(test_cases, 1):
        result = sol.groupAnagrams(strs)
        passed = normalize(result) == normalize(expected)
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: groupAnagrams({strs}) -> {result} (expected {expected}) [{status}]")