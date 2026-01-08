from collections import defaultdict, deque
# shortest transformation seq-> BFS
#状态: 当前单词 + 当前走了多少步（level）-> 某个单词上，这是第几步
#如何状态转移: 对当前单词的 每一个位置,从 'a' 到 'z' 轮流替换
# 如果： 1. 替换后 ≠ 原单词 2. 替换后的单词在 wordList 中 3.没访问过
# 两个方法做这道题: 1. 中间态映射 (下面方法) 2. 直接枚举 26 个字母
# 中间态映射: hot → *ot, h*t, ho*  dot → *ot, d*t, do*

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        # 预处理：构造“中间状态”字典
        all_combo_dict = defaultdict(list)
        word_len = len(beginWord)
        for word in wordList:
            for i in range(word_len):
                intermediate_word = word[:i] + '*' + word[i+1:]
                all_combo_dict[intermediate_word].append(word)

        # BFS 初始化
        queue = deque()
        queue.append((beginWord, 1))
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()
            for i in range(word_len):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]

                for neighbor in all_combo_dict[intermediate_word]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                # 清空防止重复访问
                all_combo_dict[intermediate_word] = []

        return 0