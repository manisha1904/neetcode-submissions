class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map.keys():
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        l, r = 0, len(self.time_map[key]) - 1
        arr = self.time_map[key]
        result = ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                r = mid - 1
            else:
                result = arr[mid][1]
                l = mid + 1
        return result
