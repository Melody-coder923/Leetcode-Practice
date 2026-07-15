1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        map=defaultdict(list)
4        for word in strs:
5            key = "".join(sorted(word))
6            map[key].append(word)
7        
8        return list(map.values())