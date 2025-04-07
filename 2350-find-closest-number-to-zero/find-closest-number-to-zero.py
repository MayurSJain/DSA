class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mind = nums[0]
        for i in nums:
            if abs(i) < abs(mind):
                mind = i
        if mind < 0 and abs(mind) in nums:
            return abs(mind)
        
        return mind

        