class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # We need to find a node that in-coming = n-1, and out-coming = 0
        # since we know that in-coming = n-1 and out-coming = 0, so diff is n-1
        track_edge_delta = defaultdict(int)
        for src,dst in trust:
            track_edge_delta[src]-=1
            track_edge_delta[dst]+=1

        for i in range(1,n+1):
            if track_edge_delta[i] == n-1:
                return i
        return -1