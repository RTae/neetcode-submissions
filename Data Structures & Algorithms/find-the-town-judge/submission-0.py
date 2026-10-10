class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # We need to find a node that in-coming = n-1, and out-coming = 0

        track_incoming = {}
        track_outcoming = {}
        judge = -1
        for t in trust:
            if t[1] in track_incoming:
                track_incoming[t[1]]+=1
            else:
                track_incoming[t[1]]=1

            if t[0] in track_outcoming:
                track_outcoming[t[0]]+=1
            else:
                track_outcoming[t[0]]=1

        for p, count in track_incoming.items():
            if count == n-1 and p not in track_outcoming:
                judge = p

        return judge