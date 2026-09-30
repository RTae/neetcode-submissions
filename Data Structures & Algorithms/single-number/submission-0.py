class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map_count = {}

        for num in nums:
            if num in map_count:
                del map_count[num]
            else:
                map_count[num] = 1
        
        return map_count.popitem()[0]