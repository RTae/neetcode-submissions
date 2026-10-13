class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # The concept is we will use bucket sort to solve this issue
        # Instead of we create a map count of value
        # We use a request map instread, since we know that we need only k top
        # mean we can return only last k output
        # {1 : 2, 2:1, 3: 4}
        # {1: [2], 2: [1], 3: [], 4: [3]}
        # Then we return [3, 1]
        map_count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            map_count[n]+=1
        
        for num, cnt in map_count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res