class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_val=min(nums)
        total=0
        while min_val:
            total+=min_val%10
            min_val=min_val//10
        return 1-total%2