class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum
        for i in range(k,n):
            curr_sum += nums[i]
            curr_sum -= nums[i-k] 
            max_sum = max(max_sum,curr_sum)
        return(max_sum/k)
    
    
