class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        n = len(nums)
        if len(nums) == 1:
            return
        for r in range(n):
            if nums[r] != 0:
                nums[r],nums[l] = nums[l],nums[r]
                l+=1
        