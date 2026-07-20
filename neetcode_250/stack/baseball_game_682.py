from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == "+":
                first = stack[-1]
                second = stack[-2]
                stack.append(first + second)
            elif i == "D":
                score = stack[-1]
                stack.append(score * 2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        
        return sum(stack)


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1"], 1),
        (["1", "C"], 0),
    ]

    for i, (ops, expected) in enumerate(test_cases, 1):
        result = sol.calPoints(ops)
        passed = result == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: calPoints({ops}) -> {result} (expected {expected}) [{status}]")