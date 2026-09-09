class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        track_score = []
        for ops in operations:
            if ops == "+":
                tmp = track_score[-1] + track_score[-2]
                track_score.append(tmp)
                res+=tmp
            elif ops == "D":
                tmp = track_score[-1]*2
                track_score.append(tmp)
                res+=tmp
            elif ops == "C":
                tmp = track_score.pop()
                res-=tmp
            else:
                track_score.append(int(ops))
                res+=int(ops)
            
        return res