# Time Complexity: O(N log 10)
# Space Complexity: O(U + T)
# Explanation: Use a hash map to map user to their followees. Use another map to map user to their tweets. For news feed, use a Max-Heap to extract the 10 most recent tweets from the user and their followees.

import heapq
import collections
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followers[userId] | {userId}
        hq = []
        for u in users:
            for t in self.tweets[u][-10:]:
                heapq.heappush(hq, t)
        return [t[1] for t in heapq.nsmallest(10, hq)]
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

