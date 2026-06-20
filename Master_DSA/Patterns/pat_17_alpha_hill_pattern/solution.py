# Time Complexity: O(N^2)
# Space Complexity: O(1)

def print_pattern(n: int) -> None:
    for i in range(n):
        spaces = " " * (n - i - 1)
        print(spaces, end="")
        ch = ord('A')
        breakpoint = (2 * i + 1) // 2
        for j in range(1, 2 * i + 2):
            print(chr(ch), end="")
            if j <= breakpoint:
                ch += 1
            else:
                ch -= 1
        print(spaces)

if __name__ == "__main__":
    print_pattern(5)

