# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    for i in range(n):
        ch = chr(ord('A') + i)
        for j in range(i + 1):
            print(ch, end=" ")
        print()

if __name__ == "__main__":
    print_pattern(5)

