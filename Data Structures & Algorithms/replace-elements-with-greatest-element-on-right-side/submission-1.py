class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            max_val = -1
            for j in range(i + 1, n):
                if arr[j] > max_val:
                    max_val = arr[j]
            arr[i] = max_val
        arr[-1] = -1
        return arr