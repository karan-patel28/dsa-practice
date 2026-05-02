class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n

        return self.fib(n - 1) + self.fib(n - 2)

if __name__ == "__main__":
    obj = Solution()

    # Example 1
    n1 = 2
    print(obj.fib(n1))  # Expected: 1

    # Example 2
    n2 = 3
    print(obj.fib(n2))  # Expected: 2

    # Example 3
    n3 = 4
    print(obj.fib(n3))  # Expected: 3