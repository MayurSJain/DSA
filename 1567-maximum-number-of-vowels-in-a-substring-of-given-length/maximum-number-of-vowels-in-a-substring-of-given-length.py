class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_v = 0
        n = len(s)
        vowel = ['a','e','i','o','u']
        for i in range(k):
            if s[i] in vowel:
                max_v += 1
        curr_v = max_v       
        for i in range(k,n):
            if max_v == k:
                return k
            if s[i-k] in vowel:
                curr_v -= 1
            if s[i] in vowel:
                curr_v += 1
            max_v = curr_v if curr_v > max_v else max_v
        return max_v
        