class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffH = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in diffH:
                return [diffH[diff], i]
            diffH[n] = i

        