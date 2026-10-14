class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            # using text lenght and append with # to be a track point
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find #
            j = s.find("#", i)
            # extract text lenght
            length = int(s[i:j])
            # then pad j+1 to j+1+lenght
            # to get a text
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res