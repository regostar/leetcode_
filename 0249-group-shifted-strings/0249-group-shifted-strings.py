class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def shift_letter(letter: str, shift: int):
            return chr((ord(letter) - shift) % 26 + ord('a'))
        
        def get_hash(string: str):
            # calculate the no of shifts required to make the first char to be 'a'
            shift = ord(string[0])
            return ''.join(shift_letter(letter, shift) for letter in string)

        # create hash val for each string and append string to list of hash
        groups = collections.defaultdict(list)

        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)
        
        return list(groups.values())