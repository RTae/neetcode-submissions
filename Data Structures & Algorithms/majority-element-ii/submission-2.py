class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counter = Counter(nums)

        for key in counter:
            if counter[key] > len(nums) // 3:
                res.append(key)
        
        return res