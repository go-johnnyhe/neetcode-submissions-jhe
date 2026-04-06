import heapq
class Twitter:
    # initialize the object
    def __init__(self):
        self.tweets_map = {}
        self.following_map = {}
        self.curr_time = 0

    # create tweetId by userId
    # hashmap of userId, list of tweetId
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_map:
            self.tweets_map[userId] = []
            self.following_map[userId] = set()
            self.following_map[userId].add(userId)
        self.tweets_map[userId].append((self.curr_time, tweetId))
        self.curr_time += 1
    # following hashmap of userId, list of userIds
    def getNewsFeed(self, userId: int) -> List[int]:
        # iterate over follower's tweet
        # build up heap of size 10
        # return those as a list
        follower_tweets = []
        if userId not in self.following_map:
            return []
        for follower in self.following_map[userId]:
            if follower not in self.tweets_map:
                continue
            for time, tweet_id in self.tweets_map[follower]:
                heapq.heappush(follower_tweets, (-time, tweet_id))
        res = []
        while len(res) < 10 and follower_tweets:
            # heapq.heappop(follower_tweets)
        # while len(follower_tweets) > 0:
            _, tweet_id = heapq.heappop(follower_tweets)
            res.append(tweet_id)
        return res

    # following hashmap
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following_map:
            self.following_map[followerId] = set()
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following_map or followeeId not in self.following_map[followerId] or followeeId == followerId:
            return
        self.following_map[followerId].remove(followeeId)
    # get a bunch of follower Ids, get their tweetIds, surface the 10 most recent
    # when would i increment time?


# for example:
# tweets map 1: [10], 2: [20]
# following map: 1: [1] 2: [2]
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
# twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].