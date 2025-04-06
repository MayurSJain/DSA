class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        m= len(s)

        if not s:
            return True
        for r in range(len(t)):
            if s[l] == t[r]:
                print(s[l])
                print(l)
                l+=1
              
            if l>=m:
                return True
        return False
        
                

        