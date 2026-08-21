class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxResult = 0
        while l < r:
            result = (r-l)* min(heights[l], heights[r])
            maxResult = max(maxResult, result)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxResult
