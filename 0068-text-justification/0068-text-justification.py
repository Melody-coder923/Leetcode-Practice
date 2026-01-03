from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0

        while i < n:
            level = []
            line_len = 0  # 当前行所有单词的总长度（不含空格）

            # 1️⃣ 尽可能往这一行里放单词
            while i < n and line_len + len(words[i]) + len(level) <= maxWidth:
                level.append(words[i])
                line_len += len(words[i])
                i += 1

            # 2️⃣ 是否是最后一行
            is_last_line = (i == n)

            # 3️⃣ 构造这一行字符串
            if len(level) == 1 or is_last_line:
                # 左对齐
                line = " ".join(level)
                line += " " * (maxWidth - len(line))
            else:
                # 两端对齐
                gaps = len(level) - 1  #几个单词间隙
                spaces = maxWidth - line_len
                ave = spaces // gaps
                addition = spaces % gaps

                line = ""
                for j in range(len(level)):
                    line += level[j]
                    if j < gaps: #决定要不要加空格,只有最后一个单词的后面不加空格
                        if j < addition:  #多余空格给谁
                            line += " " * (ave + 1)
                        else:
                            line += " " * ave

            res.append(line)

        return res
