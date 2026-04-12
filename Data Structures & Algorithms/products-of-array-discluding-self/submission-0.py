class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp = [0] * n
        rp = [0] * n
        lp[0] = 1
        
        for i in range(1, n):
            lp[i] = lp[i-1]*nums[i-1]
        rp[n-1] = 1
        for i in range(n-2,-1,-1):
            rp[i] = rp[i+1] * nums[i+1]
        res = [0] * n
        for i in range(0,n):
            res[i] = lp[i] * rp[i]
        return res