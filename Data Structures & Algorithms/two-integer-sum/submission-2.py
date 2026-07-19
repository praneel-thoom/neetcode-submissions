class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aDict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in aDict:
                return [aDict[target - nums[i]], i]
            aDict[nums[i]] = i
            
        return [0,0]