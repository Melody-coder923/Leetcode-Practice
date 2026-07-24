1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        count = defaultdict(int)
4        left = 0
5        max_len = 0
6
7        for right in range(len(fruits)):
8            count[fruits[right]] += 1
9
10            while len(count) > 2:
11                count[fruits[left]] -= 1
12                if count[fruits[left]] == 0:
13                    del count[fruits[left]]
14                left += 1
15
16            max_len = max(max_len, right - left + 1)
17
18        return max_len
19
20                
21