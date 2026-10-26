class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a==nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                threesome = a + nums[l] + nums[r]
                if threesome > 0:
                    r-=1
                elif threesome < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    # this case is for if previos left is same pointer we need to skip that, the solution will be duplicate
                    # [-2, 0, 0, 2]
                    # let's say that the l and right is add start and end
                    # we can see that when we move pointer again from 1 to 2
                    # it's a same data so we need to shift this always
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return res