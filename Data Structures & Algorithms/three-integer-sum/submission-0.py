class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        aList = []

        for S in range(len(nums) - 2):
            if S > 0 and nums[S] == nums[S-1]: continue
            L = S + 1
            R = len(nums) - 1
            while L < R:
                total = nums[S] + nums[L] + nums[R]
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    aList.append([nums[S], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]: L += 1
                    while L < R and nums[R] == nums[R-1]: R -= 1
                    L += 1
                    R -= 1
        return aList