class MyHashSet:
    def __init__(self):
        self.hashList = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashList.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashList.remove(key)

    def contains(self, key: int) -> bool:
        if self.hashList.__contains__(key):
            return True
        return False


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    # each test case is a list of (operation, args, expected_return)
    # expected_return is None for operations that don't return a checkable value (like add, remove, init)
    test_cases = [
        [
            ("add", [1], None),
            ("add", [2], None),
            ("contains", [1], True),
            ("contains", [3], False),
            ("add", [2], None),
            ("contains", [2], True),
            ("remove", [2], None),
            ("contains", [2], False),
        ],
    ]

    for i, ops in enumerate(test_cases, 1):
        hs = MyHashSet()
        all_passed = True
        results = []

        for op, args, expected in ops:
            method = getattr(hs, op)
            result = method(*args)
            if expected is not None:
                passed = result == expected
                if not passed:
                    all_passed = False
                results.append(f"{op}({', '.join(map(str, args))}) -> {result} (expected {expected})")
            else:
                results.append(f"{op}({', '.join(map(str, args))})")

        status = f"{GREEN}PASS{RESET}" if all_passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: [{status}]")
        for r in results:
            print(f"  {r}")