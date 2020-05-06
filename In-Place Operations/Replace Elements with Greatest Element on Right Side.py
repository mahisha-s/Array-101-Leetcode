#Python3
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x=[]
        for i in range(0,len(arr)-1):
            x+=[max(arr[i+1:])]
        x+=[-1]
        return x
