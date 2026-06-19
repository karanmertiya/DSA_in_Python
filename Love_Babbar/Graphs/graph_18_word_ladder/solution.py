# Time Complexity: O(N * M * 26)
# Space Complexity: O(N * M)
# Explanation: Use BFS to find the shortest path. Put the `beginWord` in a queue. For each word popped from the queue, try changing every character to all 26 lowercase letters. If the new word is in the dictionary, push it to the queue with level + 1 and remove it from dictionary to avoid cycles.

from collections import deque
def ladderLength(beginWord, endWord, wordList):
    st = set(wordList)
    q = deque([(beginWord, 1)])
    if beginWord in st: st.remove(beginWord)
    while q:
        word, steps = q.popleft()
        if word == endWord: return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in st:
                    st.remove(new_word)
                    q.append((new_word, steps + 1))
    return 0

