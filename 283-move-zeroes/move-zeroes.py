class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        n = len(nums)
        
        for r in range(n):
            if nums[r] != 0:
                nums[r],nums[l] = nums[l],nums[r]
                l+=1
        