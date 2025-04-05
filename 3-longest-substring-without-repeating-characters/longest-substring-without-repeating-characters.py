class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = set()
        i = 0
        j = 0
        n = len(s)
        maxs = 0
        for i in range(n):
            while j<=n:
                news = s[i:j+1]
                alpha = set(news)
                print(news)
                t = len(alpha)
                if t == len(news) and t > maxs:
                    maxs = t
                else:
                    break
                j+=1
            j = i + maxs + 1
        return maxs