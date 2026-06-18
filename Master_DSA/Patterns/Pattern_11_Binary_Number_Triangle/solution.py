# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    for i in range(n):
        start = 1 if i % 2 == 0 else 0
        for j in range(i + 1):
            print(start, end=" ")
            start = 1 - start
        print()

if __name__ == "__main__":
    print_pattern(5)
