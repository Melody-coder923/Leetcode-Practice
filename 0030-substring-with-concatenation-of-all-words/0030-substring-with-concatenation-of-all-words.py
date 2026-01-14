class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
            窗口步长 = word_len
            窗口大小 = word_len * len(words)
            哈希表 window[word] = 当前窗口每个单词出现次数
            当 window[word] > target[word] → 左指针右移一个单词
            当窗口内单词数 == len(words) → 匹配成功
            #1. 子串长度 
            #2.窗口如何额移动?每 次按单词长度滑动,目的是保证每次切出的子串是完整单词，不切半
            #3. hashmap统计每个单词出现次数
        """
        if not s or not words:
             return []
        word_len=len(words[0]) #steps
        word_count=len(words)
        window=word_count*word_len
        target=Counter(words)
        res=[]
        for i in range(word_len):
            left = i
            cur = Counter()
            count = 0  # 当前窗口内匹配的单词数
            for right in range(i,len(s)-word_len+1,word_len):
                # 加入新单词
                word = s[right : right + word_len]
    
                #加入新单词时，如果这个单词根本不在 target 里，直接重置窗口
                if word not in target:
                    cur.clear()
                    count = 0
                    left = right + word_len
                    continue
                # 加入新单词
                cur[word] += 1
                count += 1
                
                # 如果这个单词数量超过 target，缩小窗口直到不超
                while cur[word] > target[word]:
                    left_word = s[left : left + word_len]
                    cur[left_word] -= 1
                    if cur[left_word] == 0:
                        del cur[left_word]
                    left += word_len
                    count -= 1
                # 检查是否匹配
                if count == word_count and cur == target:
                    res.append(left)
        return res