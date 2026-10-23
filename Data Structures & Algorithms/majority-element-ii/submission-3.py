class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Using counter and check that the nunber is more than len(nums)//3
        res = []
        counter = Counter(nums)

        for key in counter:
            if counter[key] > len(nums) // 3:
                res.append(key)
        
        return res