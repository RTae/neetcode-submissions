class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # The concept is we will use bucket sort to solve this issue
        # Instead of we create a map count of value
        # We use a request map instread, since we know that we need only k top
        # mean we can return only last k output
        # {1 : 2, 2:1, 3: 4}
        # {1: [2], 2: [1], 3: [], 4: [3]}
        # Then we return [3, 1]

        map_cnt = defaultdict(int)
        freq_cnt = [[] for i in range(len(nums)+1)] 

        for n in nums:
            map_cnt[n]+=1
        for n, cnt in map_cnt.items():
            freq_cnt[cnt].append(n)
        
        res = []
        for i in range(len(freq_cnt)-1, 0, -1):
            for n in (freq_cnt[i]):     
                res.append(n)
                if len(res) == k:
                    return res