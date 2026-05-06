1class Solution:
2    def decodeString(self, s: str) -> str:
3        num_stack=[]
4        str_stack=[]
5        cur_num=0
6        cur_str = ""  
7        for ch in s:
8            if ch.isdigit():
9                cur_num = cur_num * 10 + int(ch)
10            elif ch == '[':
11                num_stack.append(cur_num)        
12                str_stack.append(cur_str)        
13                cur_num = 0
14                cur_str = ""
15            elif ch == ']':
16                repeat_times = num_stack.pop()
17                last_str = str_stack.pop()
18                cur_str = last_str + repeat_times*cur_str
19            else:
20                cur_str += ch
21        return cur_str