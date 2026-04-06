class Twitter:

    def __init__(self):
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        self._addTweetsToHeap(userId, min_heap)
        for followeeId in self.following[userId]:
            self._addTweetsToHeap(followeeId, min_heap)
        return [tweetId for _, tweetId in heapq.nlargest(10, min_heap)]

    def _addTweetsToHeap(self, userId, min_heap):
        for tweet in self.tweets[userId]:
            heapq.heappush(min_heap, tweet)


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# tweet: userId, tweetId
# news: 10 most recent tweetId from the userId (following / themself)
# follow: follower userId --> followee userId
# unfollow: follower userId --> followee userId

# Twitter: 
# - userId (int)
# - a list of followee's userIds (array)
# - a list of tweets (stack for recency?)