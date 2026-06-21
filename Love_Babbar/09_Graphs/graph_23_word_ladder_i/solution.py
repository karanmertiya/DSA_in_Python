# Time Complexity: O(N * M * 26) where N is words, M is word length
# Space Complexity: O(N)
# Explanation: BFS. Start from `beginWord`. In each step, change one character from 'a' to 'z' and check if new word is in `wordList`. If yes, push to queue, erase from `wordList` to avoid loops, and continue. Track level/steps.

import collections
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet: return 0
    q = collections.deque([(beginWord, 1)])
    if beginWord in wordSet: wordSet.remove(beginWord)
    while q:
        word, steps = q.popleft()
        if word == endWord: return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i+1:]
                if newWord in wordSet:
                    wordSet.remove(newWord)
                    q.append((newWord, steps + 1))
    return 0

