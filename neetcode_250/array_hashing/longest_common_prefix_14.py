from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        idx = 0
        word = strs[0]
        count = 0

        while idx < len(word):
            c = word[idx]
            for i in range(1,len(strs)):
                curr_word = strs[i]
                if idx < len(curr_word) and c == curr_word[idx]:
                    count += 1

            if count == len(strs) - 1:
                prefix += c
            else:
                break
            
            count = 0
            idx += 1

        return prefix


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspace", "interstellar", "interstate"], "inters"),
        (["single"], "single"),
        (["", "b", "c"], ""),
        (["same", "same", "same"], "same"),
    ]

    for i, (strs, expected) in enumerate(test_cases, 1):
        result = sol.longestCommonPrefix(strs)
        passed = result == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: longestCommonPrefix({strs}) -> {result!r} (expected {expected!r}) [{status}]")