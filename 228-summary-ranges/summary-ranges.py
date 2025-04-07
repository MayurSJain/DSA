class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        output = []
        i = 0
        while i < n:
            start = nums[i]
            while i < n-1 and nums[i] + 1 == nums[i+1]:
                    i+=1
            if start == nums[i]:
                output.append(str(nums[i]))
            else:
                output.append(str(start) + "->" + str(nums[i]))
            i+=1
        return output
            

