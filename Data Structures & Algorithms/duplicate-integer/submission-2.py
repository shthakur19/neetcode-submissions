class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numList = set(nums)

        return len(numList) != len(nums)
        