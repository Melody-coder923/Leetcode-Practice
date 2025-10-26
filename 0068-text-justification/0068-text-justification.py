class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        width = 0  # 当前行单词的总长度（不含空格）
        for word in words:
            # 判断能否加入当前行
            # width: 当前单词总长度
            # len(line): 单词间需要的最少空格数
            if line and width + len(line) + len(word) > maxWidth:
                # 当前行满了，处理这一行
                # 情况1：只有一个单词
                if len(line) == 1:
                    res.append(line[0] + ' ' * (maxWidth - width))
                else:
                    # 情况2：多个单词，需要分配空格
                    total_spaces = maxWidth - width
                    gaps = len(line) - 1

                    # 计算每个间隙的空格
                    spaces_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    # 构建这一行
                    result_line = ""
                    for i in range(len(line) - 1):
                        result_line += line[i]
                        # 基础空格 + 额外空格（前面的间隙多1个）
                        result_line += ' ' * (spaces_per_gap + (1 if i < extra_spaces else 0))
                    result_line += line[-1]  # 添加最后一个单词
                    
                    res.append(result_line)

                # 重置为新行
                line = [word]
                width = len(word)
            else:
                # 加入当前单词
                line.append(word)
                width += len(word)
        # 处理最后一行（左对齐）
        if line:
            last_line = ' '.join(line)  # 单词间只有一个空格
            res.append(last_line + ' ' * (maxWidth - len(last_line)))  # 末尾补空格

        return res