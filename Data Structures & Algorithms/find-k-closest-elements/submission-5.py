class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # the idea is we can create a k-window range to create a search range of of binary serach
        l, r = 0, len(arr)-k
        while l < r:
            m = (l+r)//2
            if x-arr[m] > arr[m+k]-x:
                l=m+1
            else:
                r=m
        return arr[l:l+k]