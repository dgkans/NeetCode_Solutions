class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map.get(key,[])
        if not vals:
            return ""
        for i in range(len(vals)-1,-1,-1):
            if vals[i][1] <= timestamp:
                return vals[i][0]
        return ""
        
        
