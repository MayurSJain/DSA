class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_window=0
        numzeros=0
        l,r=0,0
        while r < len(nums):
            if nums[r]==1:
                r+=1
            else:
                numzeros+=1
                r+=1
                if numzeros > k:
                    max_window=max(r-l,max_window)
                    while numzeros>k:
                        if nums[l]==0:
                            numzeros-=1
                        else:
                            l+=1
                    l+=1
        return max(max_window-1,r-l)