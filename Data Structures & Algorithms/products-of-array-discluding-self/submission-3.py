class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,3,4]
        # prefix pass -> res = [1, 1, 2, 6]   (product of elements LEFT of i)
        # postfix values used at i=3..0: [1, 4, 12, 24]  (product of elements RIGHT of i)
        # we can use this trick to loop over
        # final res = [24, 12, 8, 6]
        
        res=[1]*(len(nums))
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
            
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res