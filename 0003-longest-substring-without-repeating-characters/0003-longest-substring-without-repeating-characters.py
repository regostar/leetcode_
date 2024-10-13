class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we will use a sliding window and a hash for the chars inside the window
        # start from left
        left, right = 0, 0
        max_len = 0
        cur_hash = set()
        for right in range(len(s)):
            # print(cur_hash)
            if s[right] not in cur_hash:
                # until there is no repitition, add right
                max_len = max(max_len, right - left + 1)
            else:
                #pop left
                while s[right] in cur_hash:
                    # somewhere in left we have a repitition
                    cur_hash.remove(s[left])
                    left += 1
                    # print("before add ",cur_hash)
            cur_hash.add(s[right])
        return max_len
                

            
            # if s[right] in cur_hash:
            #     left = right
            #     cur_hash = set()
            
            # cur_hash.add(s[right])
            # print(cur_hash)
            # max_len = max(max_len, len(cur_hash))

            
        