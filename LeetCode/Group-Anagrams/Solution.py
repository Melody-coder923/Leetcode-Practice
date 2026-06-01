1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        map=defaultdict(list)
4        for word in strs:
5            check=tuple(sorted(word))
6            map[check].append(word)
7        return list(map.values())