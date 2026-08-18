class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore[key]
        low, high = 0, len(self.keyStore[key]) - 1

        while low <= high:
            mid = (low + high) // 2
            #0 for value, 1 for timestamp
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        
        return res