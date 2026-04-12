class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val,0)+1
        self.group[self.freq[val]].append(val)
        self.max_freq = max(self.freq[val],self.max_freq)

    def pop(self) -> int:
            ele = self.group[self.max_freq].pop()
            self.freq[ele]-=1
            if not self.group[self.max_freq]:
                self.max_freq-=1
            return ele


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()