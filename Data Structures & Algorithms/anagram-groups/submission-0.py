from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for word in strs:
            sorted_word = tuple(sorted(word))
            anagram_map[sorted_word].append(word)

        for value in anagram_map.values():
            result.append(value)

        return result
