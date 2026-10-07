class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for d in digits:
            res+=str(d)

        return [int(d) for d in str(int(res)+1)]

