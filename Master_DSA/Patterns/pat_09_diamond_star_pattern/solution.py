# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars + spaces)
    for i in range(n):
        spaces = " " * i
        stars = "*" * (2 * (n - i) - 1)
        print(spaces + stars + spaces)

if __name__ == "__main__":
    print_pattern(5)

