# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

if __name__ == "__main__":
    print_pattern(5)

