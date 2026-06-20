# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: Store the first occurrence index of all characters. Iterate the string, for each character check if there is a lexicographically smaller character that appears later in the string. If so, swap them and break.

def chooseandswap(a):
    s = set(a)
    for i in range(len(a)):
        if a[i] in s: s.remove(a[i])
        if not s: break
        min_char = min(s)
        if min_char < a[i]:
            ch1, ch2 = a[i], min_char
            a = a.replace(ch1, '#')
            a = a.replace(ch2, ch1)
            a = a.replace('#', ch2)
            break
    return a

