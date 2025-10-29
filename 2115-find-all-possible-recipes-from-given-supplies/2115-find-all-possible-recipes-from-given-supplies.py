class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        #建立菜谱名字 -> index 映射
        recipe_index = {recipe: i for i, recipe in enumerate(recipes)}
        #初始化入度表: 只有为0才可以做出来, 初始化为0, [0]
        indegree=[0]*len(recipes) 
        #更新入度表和建立前置关系表
        prerequire=defaultdict(list)
        for index_recipe,items in enumerate(ingredients):  #[["yeast","flour"]]
            indegree[index_recipe]+=(len(items))  #indegree [2]
        # 前置条件->recipt
            for item in items:
                prerequire[item].append(index_recipe) #("yeast": 0 ,"flour": 0)   item: index of bread
                
        #supplie 放入队列弹出更新入度表 ["yeast","flour","corn"]
        q=deque(supplies) 
        res=[]
        while q:
            item=q.popleft() 
            # 如果当前 item 是菜谱，加入结果
            if item in recipes:
                res.append(item)
            #更新indegree表
            for index_recipe in prerequire.get(item, []):
                indegree[index_recipe]-=1
                if indegree[index_recipe] == 0:
                    q.append(recipes[index_recipe]) 
        return res
        