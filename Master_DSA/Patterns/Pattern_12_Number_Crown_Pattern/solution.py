# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    space = 2 * (n - 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print(" " * space, end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()
        space -= 2

if __name__ == "__main__":
    print_pattern(5)
