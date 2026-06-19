# Time Complexity: O(N * L * 26) where L is word length
# Space Complexity: O(N)
# Explanation: Use BFS. Insert words from `wordList` into a hash set for O(1) lookup. Push `{beginWord, 1}` to a queue and remove it from the set. Pop a word, change each character one by one to 'a'-'z'. If the new word is in the set, push `{newWord, steps+1}` and remove from set. If `newWord == endWord`, return `steps+1`.

import collections
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
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

