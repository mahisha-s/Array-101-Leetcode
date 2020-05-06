#Python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)):
            if(i!=nums.index(nums[i])):
                del nums[i]
            else:
                i+=1
        return len(nums)
