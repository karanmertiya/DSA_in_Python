# Time Complexity: O(V + E + Paths)
# Space Complexity: O(V + E)
# Explanation: BFS to find minimum steps to reach each word. Then DFS starting from `endWord` backwards to `beginWord`, only exploring paths where `dist[next_word] == dist[curr_word] - 1`. Reverse the built paths.

import collections
def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordSet = set(wordList)
    if endWord not in wordSet: return []
    q = collections.deque([beginWord])
    mpp = {beginWord: 1}
    wordSet.discard(beginWord)
    while q:
        word = q.popleft()
        if word == endWord: break
        steps = mpp[word]
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i+1:]
                if newWord in wordSet:
                    mpp[newWord] = steps + 1
                    q.append(newWord)
                    wordSet.remove(newWord)
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
                    if newWord in mpp and mpp[newWord] + 1 == steps:
                        seq.append(newWord)
                        dfs(newWord, seq)
                        seq.pop()
        dfs(endWord, [endWord])
    return ans

