class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum
        for i in range(k,len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i-k] 
            max_sum = curr_sum if curr_sum > max_sum else max_sum
        return(max_sum/k)
    
    
