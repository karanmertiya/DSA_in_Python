# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    iniSpace = 0
    for i in range(n):
        print("*" * (n - i) + " " * iniSpace + "*" * (n - i))
        iniSpace += 2
    iniSpace = 2 * n - 2
    for i in range(1, n + 1):
        print("*" * i + " " * iniSpace + "*" * i)
        iniSpace -= 2

if __name__ == "__main__":
    print_pattern(5)
