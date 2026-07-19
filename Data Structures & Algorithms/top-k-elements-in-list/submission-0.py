class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aDict = Counter(nums)
        aList = aDict.most_common(k)
        return [aList[n][0] for n in range(len(aList))]