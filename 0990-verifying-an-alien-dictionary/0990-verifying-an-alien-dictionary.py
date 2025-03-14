class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # lexicographical sorting means ascending order of strings
        # given order map and words, we check if words are LS or not

        # we have the order given, we convert that to dict
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(words[i])):
            # if no mismatch at all, then we need to example words like 
            # app apple
            # left one must always be smaller than right
                if j == len(w2):
                    return False
                    # apple app - space has less order than anything
                if w1[j] != w2[j]:
                    # mismatch
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    # Now if we find first different character and it's sorted
                    # no need of checking the remaining letters
                    break
                    # ex - juzce juizz is still sorted
        return True
            

        