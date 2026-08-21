class Solution:
    def findMin(self, nums: List[int]) -> int:
        sz = len(nums)
        l=0
        r=len(nums)
        res = 0
        mid = int((r-l)/2)
        while nums[mid]> nums[mid-1]:
             mid -= 1
        if nums[r-1]< nums[mid]:
            res = min(nums[mid:r])
        elif nums[l]< nums[mid]:
            res = min(nums[l:mid+1])
        else:
            res = nums[mid]
        return res

        