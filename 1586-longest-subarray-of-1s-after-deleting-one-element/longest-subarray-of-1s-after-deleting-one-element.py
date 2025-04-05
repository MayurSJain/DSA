class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r = 0,0
        zeros = 0
        max_win = 0
        n = len(nums)
        while r < n:
            if nums[r]==1:
                r+=1
            else:
                zeros+=1
                r+=1
                max_win = max(r-l-1,max_win)
                if zeros > 1:
                    while zeros > 1:
                        if nums[l] == 0:
                            zeros -= 1
                        else:
                            l+=1
                    l+=1
        return(max(max_win - 1, r - l - 1))
        