# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    spaces = 2 * n - 2
    for i in range(1, 2 * n):
        stars = i if i <= n else 2 * n - i
        print("*" * stars + " " * spaces + "*" * stars)
        if i < n:
            spaces -= 2
        else:
            spaces += 2

if __name__ == "__main__":
    print_pattern(5)

