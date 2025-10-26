class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count=Counter(s)
        stack=[]
        in_stack=set()
        for char in s:
            count[char] -= 1
            if char in in_stack:
                continue
            # 贪心：能否删除栈顶字符？
            # 条件1：栈顶字符 > 当前字符（删除它能让字典序更小）
            # 条件2：栈顶字符后面还会出现（删除它不会丢失这个字符）
            while stack and stack[-1] > char and count[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(char)
            in_stack.add(char)
        return ''.join(stack)