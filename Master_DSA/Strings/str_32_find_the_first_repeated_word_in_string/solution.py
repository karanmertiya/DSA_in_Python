# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Split the string into words. Iterate through the words. If a word is already in the hash set, it is the first repeated word. Return it. Else, add it to the hash set.

def firstRepeatedWord(s):
    import re
    words = re.findall(r'\w+', s)
    st = set()
    for word in words:
        if word in st: return word
        st.add(word)
    return "No Repetition"

