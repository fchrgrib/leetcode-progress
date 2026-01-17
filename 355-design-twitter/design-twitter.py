class Tweet:

    def __init__(self, tweet_id: int, time: int):
        self.tweet_id = tweet_id
        self.time = time
    
    def __lt__(self, other):
        return self.time < other.time

class User:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.tweet: List[Tweet] = []
        self.following: List[int] = []
    
    def post(self, tweet_id: int, time: int):
        self.tweet.append(Tweet(tweet_id, -time))
    
    def follow(self, user: int):
        self.following.append(user)
    def unfollow(self, user: int):
        if user not in self.following:
            return
        self.following.remove(user)
    def get_tweet(self):
        return self.tweet
    
    def get_following(self):
        return self.following
    
    def __str__(self):
        return self.user_id
    



class Twitter:

    def __init__(self):
        self.time = 0
        self.user_map = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.validate_user(userId)
        self.user_map[userId].post(tweetId, self.time)
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.validate_user(userId)
        k = 10
        heap = []
        res = []
        visit = set()

        for i in self.user_map[userId].get_tweet():
            if i in visit:
                continue
            heapq.heappush(heap, i)
            visit.add(i)
        for i in self.user_map[userId].get_following():
            for j in self.user_map[i].get_tweet():
                if j in visit:
                    continue
                heapq.heappush(heap, j)
                visit.add(j)
        while heap and k>0:
            res.append(heapq.heappop(heap).tweet_id)
            k-=1
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.validate_user(followerId)
        self.validate_user(followeeId)
        self.user_map[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.validate_user(followerId)
        self.validate_user(followeeId)
        self.user_map[followerId].unfollow(followeeId)

    def validate_user(self, user_id: int):
        if user_id in self.user_map:
            return
        
        self.user_map[user_id] = User(user_id)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)