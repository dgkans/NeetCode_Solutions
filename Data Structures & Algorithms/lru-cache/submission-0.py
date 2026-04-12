class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict.pop(key)
            self.dict[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        if len(self.dict) == self.capacity:
            del self.dict[next(iter(self.dict))]
        self.dict[key] = value
