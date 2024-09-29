class AllOne:

    def __init__(self):
        self.lookup = collections.defaultdict(set)
        self.count = {}
        self.maxIndex = 0
        self.minIndex = 0
        

    def inc(self, key: str) -> None:
        if key not in self.count:
            self.count[key ] = 1
            self.lookup[1].add(key)
            self.minIndex = 1
            if self.maxIndex < 1:
                self.maxIndex = 1
        else:
            self.lookup[self.count[key]].remove(key)
            if self.minIndex == self.count[key] and len(self.lookup[self.count[key]]) == 0:
                self.minIndex += 1
            self.count[key] += 1
            self.lookup[self.count[key]].add(key)
            if self.count[key] > self.maxIndex:
                self.maxIndex = self.count[key]
        

    def dec(self, key: str) -> None:
        self.lookup[self.count[key]].remove(key)
        if self.minIndex == self.count[key] and len(self.lookup[self.count[key]]) == 0:
            self.minIndex -= 1
        if self.count[key] == self.maxIndex and len(self.lookup[self.count[key]]) == 0:
            self.maxIndex -= 1
        self.count[key] -= 1
        
        if self.count[key] > 0:
            self.lookup[self.count[key]].add(key)
        else:
            del self.count[key]
        
        

    def getMaxKey(self) -> str:
        if len(self.lookup[self.maxIndex]) > 0:
            return next(iter(self.lookup[self.maxIndex]))
        return ""
        

    def getMinKey(self) -> str:
        if len(self.lookup[self.minIndex]) > 0:
            return next(iter(self.lookup[self.minIndex]))
        if self.minIndex == 0 and len(self.count) > 0:
            while len(self.lookup[self.minIndex]) == 0:
                self.minIndex += 1
            return next(iter(self.lookup[self.minIndex]))
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
