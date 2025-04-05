class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        zeros = []
        max_one = 0
        curr_zero = 0
        for r in range(n):
            if nums[r] == 0:
                zeros.append(r)
                if curr_zero < k:
                    curr_zero += 1
                else:
                    l = zeros[0] + 1
                    zeros.pop(0)
            win = (r-l) + 1
            max_one = max(win, max_one)
        return max_one

        