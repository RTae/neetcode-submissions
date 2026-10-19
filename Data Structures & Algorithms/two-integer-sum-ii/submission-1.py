class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer concept and since our numbers is sorted 
        # if our value more than target we can shif right
        # if our value is less than our target we can do left shift

        l, r = 0, len(numbers)-1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r-=1
            elif curr_sum < target:
                l+=1
            else:
                return [l+1,r+1]
        
        return []