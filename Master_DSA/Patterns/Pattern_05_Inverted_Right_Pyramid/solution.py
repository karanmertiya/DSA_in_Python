# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    for i in range(n, 0, -1):
        print("* " * i)

if __name__ == "__main__":
    print_pattern(5)
