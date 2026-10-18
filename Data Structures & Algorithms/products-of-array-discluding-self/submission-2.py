class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the idea is we can use prefix or postfix
        # then we will use the prefix_i-1 and postfix_i+i and do a product of it
        
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