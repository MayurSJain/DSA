class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s = sum(nums[:k])
        cur_s = max_s
        for i in range(k,len(nums)):
            cur_s += nums[i]
            cur_s -= nums[i-k]
            max_s = cur_s if cur_s > max_s else max_s
        return max_s/k