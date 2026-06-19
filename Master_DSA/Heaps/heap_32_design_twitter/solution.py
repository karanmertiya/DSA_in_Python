# Time Complexity: O(K log K) for feed where K is 10.
# Space Complexity: O(Total Tweets + Follow Relations)
# Explanation: Maintain a timestamp for tweets. Each user has a list of tweets and a set of followed users. To get the news feed, gather the most recent tweets from the user and all followees using a max-heap (like merging K sorted lists).

import collections
import heapq
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = collections.defaultdict(list)
        self.followees = collections.defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followees[userId] | {userId}
        heap = []
        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                t, tweetId = self.tweets[u][idx]
                heapq.heappush(heap, (-t, tweetId, u, idx - 1))
        res = []
        while heap and len(res) < 10:
            _, tweetId, u, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                t, nxtTweetId = self.tweets[u][idx]
                heapq.heappush(heap, (-t, nxtTweetId, u, idx - 1))
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

