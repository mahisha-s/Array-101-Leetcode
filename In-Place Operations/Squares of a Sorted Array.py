#Python3
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l=[x*x for x in A]
        l.sort()
        return l
        
