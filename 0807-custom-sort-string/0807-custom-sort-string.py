from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # itewrate elemnts of order
        # chjeck if each is present in set(str)
        # add to final
        freq = Counter(s)
        result = ''
        anyorder = ''
        for each in order:
            if each in freq:
                result += each * freq[each]
        order_set = set(order)
        for key, val in freq.items():
            if key not in order_set:
                anyorder += key * val
        return result + anyorder

        