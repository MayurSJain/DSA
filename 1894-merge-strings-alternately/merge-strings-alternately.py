class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op = ""
        i,j = 0,0
        cntr = 0
        while i < len(word1) and j < len(word2):
            if cntr % 2 == 0:
                op = op + word1[i]
                i = i + 1
            else:
                op = op + word2[j]
                j = j + 1
            cntr = cntr + 1
        
        while i < len(word1):
            op = op + word1[i]
            i = i + 1
        
        while j < len(word2):
            op = op + word2[j]
            j = j + 1
        
        return op