class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        i = 0
        while i < len(nums):
            if nums[i] not in temp:
                temp.append(nums[i])
            else:
                return True
            i+=1
        
        return False