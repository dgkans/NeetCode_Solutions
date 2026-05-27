class MyHashMap:

    def __init__(self):
        self.hash = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value

    def get(self, key: int) -> int:
        return self.hash[key]

    def remove(self, key: int) -> None:
        self.hash[key] = -1