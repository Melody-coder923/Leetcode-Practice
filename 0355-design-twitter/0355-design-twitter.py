class Twitter:

    def __init__(self):
        self.time = 0  # 全局时间戳
        self.tweets = defaultdict(list)   # userId -> heap[(time, tweetId)]
        self.following = defaultdict(set) # userId -> set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (-self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feed=[]
        heap=[]
        users = self.following[userId] | {userId}
        # 将所有人的最新推文放入一个大堆
        for uid in users:
            for time, tid in self.tweets[uid]:
                heapq.heappush(heap, (time, tid))
        # 取出最新的 10 条
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)