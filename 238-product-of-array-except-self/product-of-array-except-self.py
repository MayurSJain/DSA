class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fix = 1
        output = []
        for i in range(n):
            output.append(fix)
            fix *= nums[i]
        fix = 1
        for i in range(n-1,-1,-1):
            output[i] *= fix
            fix *= nums[i]
        return output