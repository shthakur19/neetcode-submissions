class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            numFreq[n] = 1 + numFreq.get(n,0)
        for n,cnt in numFreq.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res