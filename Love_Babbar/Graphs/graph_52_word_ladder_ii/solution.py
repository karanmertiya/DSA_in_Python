# Time Complexity: O(N * L * 26 + Paths)
# Space Complexity: O(N * L)
# Explanation: First, use BFS to build a map storing the shortest distance from `beginWord` to every reachable word. Then use DFS starting from `endWord` backwards to `beginWord` to reconstruct the paths. In DFS, only traverse to words whose distance is exactly 1 less than the current word's distance.

import collections
def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordSet = set(wordList)
    mpp = {beginWord: 1}
    q = collections.deque([beginWord])
    if beginWord in wordSet: wordSet.remove(beginWord)
    while q:
        word = q.popleft()
        steps = mpp[word]
        if word == endWord: break
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i+1:]
                if newWord in wordSet:
                    wordSet.remove(newWord)
                    q.append(newWord)
                    mpp[newWord] = steps + 1
    ans = []
    if endWord in mpp:
        def dfs(word, seq):
            if word == beginWord:
                ans.append(seq[::-1])
                return
            steps = mpp[word]
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in mpp and mpp[newWord] == steps - 1:
                        dfs(newWord, seq + [newWord])
        dfs(endWord, [endWord])
    return ans

