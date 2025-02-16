class RecentCounter:

    def __init__(self):
        self.reqTimes = deque()

    def ping(self, t: int) -> int:
        self.reqTimes.append(t)

        while self.reqTimes[0] < t - 3000:
            self.reqTimes.popleft()
        
        return len(self.reqTimes)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)