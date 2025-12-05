class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for word in strs:
            check=tuple(sorted(word))
            map[check].append(word)
        return list(map.values())