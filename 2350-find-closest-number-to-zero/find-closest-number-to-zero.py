class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mind = abs(nums[0])
        maxe = nums[0]
        for i in nums:
            temp = abs(i - 0)
            if temp < mind:
                mind = temp
                maxe = i
            elif temp==mind:
                if maxe < i:
                    maxe = i
        return maxe

        