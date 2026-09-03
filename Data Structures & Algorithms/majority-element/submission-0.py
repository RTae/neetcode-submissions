class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for i in nums:
            if i in map:
                map[i]+=1
            else:
                map[i] = 1
        max_num = -1
        max_num_idx = 0
        for i,cnt in map.items():
            if cnt >= max_num:
                max_num = cnt
                max_num_idx=i
        
        return max_num_idx