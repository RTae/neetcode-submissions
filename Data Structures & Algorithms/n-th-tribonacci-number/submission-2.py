class Solution:
    def tribonacci(self, n: int) -> int:

        cache = [-1] * n
        
        def recur(i):
            if i <= 2:
                return 1 if n != 0 else 0
            
            if cache[i] != -1:
                return cache[i]

            cache[i] = recur(i-3)+recur(i-2)+recur(i-1)
        
            return cache[i]
        
        return recur(0)