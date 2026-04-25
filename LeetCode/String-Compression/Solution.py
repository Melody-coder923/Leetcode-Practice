1class Solution:
2    def compress(self, chars: List[str]) -> int:
3        write=0
4        i=0
5        while i< len(chars):
6            current_char=chars[i]
7            count=1
8            while i+1< len(chars) and chars[i+1]==current_char:
9                count+=1
10                i+=1
11            chars[write]=current_char
12            write+=1
13            if count>1:
14                for num in str(count):
15                    chars[write]=num
16                    write+=1
17            i+=1
18        return write
19        
20                