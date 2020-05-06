#Python3
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in A:
            if(i%2==0):
                e+=[i]
            else:
                o+=[i]
        return (e+o)
        
