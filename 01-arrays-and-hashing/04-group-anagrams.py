# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Solution #1
        # groups = {}
        # for s in strs:
        #     s_sorted = "".join(sorted(s))
        #     if s_sorted in groups:
        #         groups[s_sorted].append(s)
        #     else:
        #         groups[s_sorted] = [s]
        # return list(groups.values())

        # Solution #2
        groups = defaultdict(list) # mapping charCount to list of anagrams
        for s in strs:
            count = [0] * 26 # a..z
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return groups.values()