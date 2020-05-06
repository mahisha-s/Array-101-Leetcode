#Python3
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        double=[i*2 for i in arr]
        x=list(set(double).intersection(arr))
        if(x==[]):
            return False
        else:
            if(len(x)==1 and x[0]==0 and arr.count(0)==1):
                return False
            else:
                return True
