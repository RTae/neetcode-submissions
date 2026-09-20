class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        count_num = []
        for num in arr:
            if num+1 in arr and num+1 not in count_num:
                count+=1
                count_num.append(num+1)

        return count            