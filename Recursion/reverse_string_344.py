from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        self.recursion(s, left, right)

    def recursion(self, s, left, right):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]

        self.recursion(s, left + 1, right - 1)


if __name__ == "__main__":
    obj = Solution()

    # Example 1
    s1 = ["h","e","l","l","o"]
    obj.reverseString(s1)
    print(s1)  # Expected: ["o","l","l","e","h"]

    # Example 2
    s2 = ["H","a","n","n","a","h"]
    obj.reverseString(s2)
    print(s2)  # Expected: ["h","a","n","n","a","H"]