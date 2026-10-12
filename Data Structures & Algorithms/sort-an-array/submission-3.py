class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Apply mergeSort by using divide and conquer concept

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            # do a basic compare which value is smaller and put it
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1
            while j < len(left):
                arr[i] = left[j]
                j+=1
                i+=1
            while k < len(right):
                arr[i] = right[k]
                k+=1
                i+=1

        def mergeSort(arr, l, r):
            # if problem have a unit of 1 it mean it's cannot break anymore
            if l >= r:
                return

            m = (l+r)//2
            # break down the problem into smaller problem and solve it
            # recursive a problem in each level
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            # then do a merge and sort
            merge(arr, l, m, r)
        
        mergeSort(nums, 0, len(nums)-1)
        return nums