#Python3
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        m=0
        while(i<=n-1):
            while(i<=n-1 and nums[i]!=1):
                i+=1
            s=i
            while(i<=n-1 and nums[i]==1):
                i+=1
            e=i
            m=max(m,e-s)
        return m
