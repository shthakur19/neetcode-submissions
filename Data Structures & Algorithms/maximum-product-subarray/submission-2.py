class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1

        for i in nums:
            temp = currMax * i
            currMax = max(i, currMax * i, currMin * i)
            currMin = min(i, temp, currMin * i)
            res = max(res, currMax)
        return res
        
