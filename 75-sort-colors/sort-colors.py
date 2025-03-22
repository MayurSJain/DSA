class Solution:
    def sortColors(self, nums: List[int]) -> None:
       l = [0,0,0]
       for i in nums:
        l[i] += 1
       index = 0
       for i in range(3):
        while l[i]!=0:
            nums[index] = i
            index += 1
            l[i] -= 1
                
        
       
       