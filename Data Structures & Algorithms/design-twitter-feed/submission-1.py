from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.graph = defaultdict(set) # followee -> followers
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.count))        
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        people = self.graph[userId] | {userId}
        for followeeId in people:
            if self.tweets[followeeId]:
                tweetId, sortKey = self.tweets[followeeId][-1]
                idx = len(self.tweets[followeeId]) - 1
                heapq.heappush(heap, (-sortKey, followeeId, tweetId, idx))
        res = []
        while heap: 
            _, followeeId, t, idx = heapq.heappop(heap)
            res.append(t)
            if len(res) == 10:
                return res
            if idx != 0:
                tweetId, sortKey = self.tweets[followeeId][idx - 1]
                heapq.heappush(heap, (-sortKey, followeeId, tweetId, idx - 1))
        
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.graph[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.graph[followerId].discard(followeeId)
        
