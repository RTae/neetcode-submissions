class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer concept and since our numbers is sorted 
        # if our value more than target we can shif right
        # if our value is less than our target we can do left shift

        l, r = 0, len(numbers)-1

        # check until l pointer is more than right
        while l < r:
            curr_sum = numbers[l] + numbers[r]

            # if our sum is more than target it's mean we sum more than we need do a right shift
            if curr_sum > target:
                r-=1
            # if our sum is less than target it's mean we sum less than we need do a left shift
            elif curr_sum < target:
                l+=1
            # found it return with index plus+1, since it's a problem requirement
            else:
                return [l+1,r+1]
        # does not found retuen a empty array
        return []