class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # we need to check a duplicate data in hash set in giving window
        # return true when we found a duplicate data in giving window
        
        window = set()
        l = 0
        for r in range(len(nums)):
            # if index range is more than k range shift the window
            if r-l > k:
                window.remove(nums[l])
                l+=1
            # if we found a dup in giving k, return true
            if nums[r] in window:
                return True
            # keep adding a data to track
            window.add(nums[r])
        
        # there is no data that satify this condition
        return False