class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        # Create a map between two word, so we don't need to do a search
        
        word_map = defaultdict(set)
        for w1, w2 in similarPairs:
            word_map[w1].add(w2)
            word_map[w2].add(w1)

        for s1 in sentence1:
            if word_map[s1] in sentence2 or s1 in sentence2:
                continue
            
            return False


        return True