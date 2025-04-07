class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        l = strs[0]
        r = strs[len(strs)-1]
        ans = ""
        for i in range(min(len(l), len(r))):
            if l[i] == r[i]:
                ans += l[i]
            else:
                break
        return ans
        