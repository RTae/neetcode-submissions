class Solution:
    def tribonacci(self, n: int) -> int:

        cache = [-1] * n
        
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        cache[0]=0
        cache[1]=1
        cache[2]=1

        def recur(i):
            
            if i >= n:
                return i == n

            if cache[i] != -1:
                return cache[i]

            cache[i] = recur(i+3)+recur(i+2)+recur(i+1)
        
            return cache[i]
        
        return recur(0)