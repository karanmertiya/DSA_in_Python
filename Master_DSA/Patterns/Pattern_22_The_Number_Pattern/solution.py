# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top = i
            left = j
            right = (2 * n - 2) - j
            down = (2 * n - 2) - i
            print(n - min(top, left, right, down), end=" ")
        print()

if __name__ == "__main__":
    print_pattern(4)
