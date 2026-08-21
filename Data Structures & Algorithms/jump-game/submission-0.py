class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpsize = 0

        for i in range(len(nums)-1,0,-1):
            if nums[i-1] >= jumpsize + 1:
                jumpsize = 0
            else:
                jumpsize += 1
        
        return nums[0] >= jumpsize

        