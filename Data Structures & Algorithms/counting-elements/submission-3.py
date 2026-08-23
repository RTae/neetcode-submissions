class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        # count_num logic was flawed as it tracked the target instead of the source index
        # Converting to a set for O(1) lookups is standard optimization
        arr_set = set(arr)
        for num in arr:
            if num + 1 in arr_set:
                count += 1

        return count