class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        pairs = self.map[key]
        # target is timestamp
        lo, hi = 0, len(pairs) - 1
        result = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            
            if pairs[mid][1] <= timestamp:
                result = pairs[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1

        return result

        
