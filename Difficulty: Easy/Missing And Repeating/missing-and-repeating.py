

class Solution:
    def findTwoElement( self,arr): 
        l = [0]* (len(arr) + 1)
        for i in arr:
            l[i] += 1
        j = [0,0]  
        for i in range(1,len(l)):
            if l[i] == 2:
                j[0] = i
            if l[i] == 0:
                j[1] = i
                
        return j
                
                
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends