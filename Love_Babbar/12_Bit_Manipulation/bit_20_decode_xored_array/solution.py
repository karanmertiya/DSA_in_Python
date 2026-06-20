# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Since `encoded[i] = arr[i] ^ arr[i+1]`, it implies `arr[i+1] = arr[i] ^ encoded[i]`. We have `arr[0]`, so we can iteratively find the rest.

def decode(encoded: list[int], first: int) -> list[int]:
    arr = [0] * (len(encoded) + 1)
    arr[0] = first
    for i in range(len(encoded)):
        arr[i+1] = arr[i] ^ encoded[i]
    return arr

