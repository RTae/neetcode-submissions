class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        # Create a map between two word, so we don't need to do a search
        word_map = defaultdict(set)
        for w1, w2 in similarPairs:
            word_map[w1].add(w2)
            word_map[w2].add(w1)

        # map one by one
        for i in range(len(sentence1)):
            # Check if word already same or word from sentence 2 in map
            if sentence1[i] == sentence2[i] or sentence2[i] in word_map[sentence1[i]]:
                continue
            return False


        return True