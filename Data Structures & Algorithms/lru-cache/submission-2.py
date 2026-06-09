class LRUCache:


    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.order = defaultdict(int)
        self.idx = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        self.order[key] = self.idx
        self.idx += 1
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys() or len(self.cache) < self.capacity:
            self.cache[key] = value
            self.order[key] = self.idx
            self.idx += 1
            return
        
        min_val_key, min_val = float("inf"), float("inf")
        for k, v in self.order.items():
            if v < min_val:
                min_val_key = k
                min_val = v
        
        del(self.cache[min_val_key])
        del(self.order[min_val_key])
        self.cache[key] = value
        self.order[key] = self.idx
        self.idx += 1
        