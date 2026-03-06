1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack=list()
4        ops = {
5            "+":lambda a,b:a+b,
6            "/":lambda a,b:int(a/b),
7            "-":lambda a,b:a-b,
8            "*":lambda a,b:a*b
9        }
10        for item in tokens:
11            if item not in ["+","-","*", "/"]:
12                stack.append(int(item))
13            else:
14                num2=stack.pop() 
15                num1=stack.pop()
16                result = ops[item](num1,num2)
17                stack.append(result)
18        return stack.pop()