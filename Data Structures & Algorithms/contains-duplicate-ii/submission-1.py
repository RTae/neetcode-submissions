class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # we need to loop check from left to right
        # if we find a same number just check it less than k
        # if not let keep moving windown
        
        window = set()
        l = 0
        for r in range(len(nums)):
            if r-l > k:
                window.remove(nums[l])
                l+=1

            if nums[r] in window:
                return True
            # add a data in nums to keep track
            window.add(nums[r])
        
        # there is no data that satify this condition
        return False