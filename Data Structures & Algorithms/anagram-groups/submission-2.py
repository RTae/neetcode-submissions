class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the idea is we can use a hash map to create a map of same word
        # [count of char] : [group of word] 
        # [1,1,.0.,0] : [ab, ba]
        
        # Mapping char count into a list of anagrams
        res = defaultdict(list)

        for s in strs:
            count = [0]*26 # a->z

            for c in s:
                # set mapping to start at zero and count this char
                count[ord(c)-ord("a")]+=1

            # we will get something like
            # if s is ab, we get [1,1,...,0]
            # if next s is ba, we also get [1,1,...,0]
            # we can use this to make a map

            res[tuple(count)].append(s)

        return list(res.values())
