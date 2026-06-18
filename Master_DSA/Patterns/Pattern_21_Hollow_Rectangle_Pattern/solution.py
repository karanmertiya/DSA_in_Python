# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    print_pattern(5)
