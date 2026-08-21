class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffSet = {}
        for i, n in enumerate(nums):
            if n in diffSet:
                return [diffSet[n],i]
            else:
               diffSet[target-n] = i
            

        