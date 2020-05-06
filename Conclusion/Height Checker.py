#Python3
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s=heights[:]
        s.sort()
        c=0
        for i in range(0,len(heights)):
            if(heights[i]!=s[i]):
                c+=1
        return c
        
