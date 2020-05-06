#Python3
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(A==[]):
            return False
        else:
            m=A.index(max(A))
            i=0
            if(m==0 or m==len(A)-1):
                return False
            else:
                while(i<m):
                    if(A[i]<A[i+1]):
                        i+=1
                    else:
                        return False
                while(i<len(A)-1):
                    if(A[i]>A[i+1]):
                        i+=1
                    else:
                        return False
            return True
