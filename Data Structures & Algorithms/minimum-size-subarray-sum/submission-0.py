class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, cur_sum = 0,0
        min_len = float('inf')
        for right in range(len(nums)):
            cur_sum +=nums[right]
            while cur_sum >= target:
                if right - left + 1 < min_len:
                    min_len= right-left+1
                cur_sum -=nums[left]
                left+=1
        if min_len != float('inf'):
            return min_len
        else:
            return 0
        