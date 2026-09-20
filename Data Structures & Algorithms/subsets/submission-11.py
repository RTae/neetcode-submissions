class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            size = len(res)
            for i in range(size):
                subset = res[i]
                subset.append(num)
                res.append(subject)
        
        return res