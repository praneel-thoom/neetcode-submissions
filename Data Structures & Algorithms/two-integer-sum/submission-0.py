class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in numDict:
                return[numDict[difference], index] 
            numDict[num] = index
        