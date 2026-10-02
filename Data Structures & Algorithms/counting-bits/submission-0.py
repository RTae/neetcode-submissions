class Solution:
    def countBits(self, n: int) -> List[int]:
        res = 0
        nums = [j for j in range(n+1)]
        res = [0]*len(nums)
        for idx, num in enumerate(nums):
            temp = num
            count = 0
            while temp:
                temp &= temp-1
                count+=1
            res[idx]=count
        
        return res