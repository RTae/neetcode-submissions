class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums1:
                idx = nums2.index(i)
                res.append(idx)
        
        return res