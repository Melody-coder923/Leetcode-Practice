1class Solution:
2    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
3        #input： 1-9， k: how many numbers , n : sum
4        # combination -> backtracking 
5        res=[]
6        def backtrack(start,path,target):
7            #base case
8            if len(path)==k:
9                if target==0:
10                    res.append(path[:])
11                return
12            # 循环
13            for num in range(start,10):
14                if target-num<0:
15                    break
16                path.append(num)
17                backtrack(num+1,path,target-num)
18            #backtrack
19                path.pop()
20        backtrack(1,[],n)
21        return res
22    
23  