# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    for i in range(n):
        for j in range(n - i):
            print(chr(ord('A') + j), end=" ")
        print()

if __name__ == "__main__":
    print_pattern(5)

