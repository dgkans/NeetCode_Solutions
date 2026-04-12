class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map.get(key,[])
        if not vals:
            return ""
        low = 0
        high = len(vals)-1
        while low <=high:
            mid = (low + high)//2
            if vals[mid][1] == timestamp:
                return vals[mid][0]
            elif vals[mid][1]>timestamp:
                high = mid - 1
            else:
                low = mid + 1
        return vals[high][0] if high>=0 else ""
                
        
        
