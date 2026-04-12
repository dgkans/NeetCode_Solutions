class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbersMap = {}
        freq = []
        for i in range (len(nums)+1):
            freq.append([])
        
        for n in nums:
            numbersMap[n] = 1 + numbersMap.get(n, 0)
        for number, freqCount  in numbersMap.items():
            freq[freqCount].append(number)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
