# Time Complexity: O(N log N) (Trade-off)
# Space Complexity: O(1) or O(N) (Language dependent)
# Explanation: Sort both strings and compare if they are identical.

def is_anagram_brute(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    return sorted(s) == sorted(t)

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Use a fixed size frequency array (Hash Map) to count character occurrences.

def is_anagram_optimal(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    for c in count:
        if c != 0: return False
    return True

