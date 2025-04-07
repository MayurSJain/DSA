class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        num = 0
        dicts = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        for i in range(n-1,-1,-1):
            num += dicts[s[i]]
            if i-1 >= 0:
                if (s[i] == 'V' or s[i] == 'X') and s[i-1] == 'I':
                    num-=2
                elif (s[i] == 'L' or s[i] == 'C') and s[i-1] == 'X':
                    num-=20        
                elif (s[i] == 'D' or s[i] == 'M') and s[i-1] == 'C':
                    num-=200
        return num
        