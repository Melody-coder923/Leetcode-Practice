class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #从离终点最近的车开始，后面的车追上前面的车时形成车队
        # 按位置降序排列
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]

        stack = []
        for t in times:
            # 如果栈为空，或者当前车时间 > 栈顶，说明形成新车队
            if not stack or t > stack[-1]:
                stack.append(t)
            # 否则归入前车队，不入栈也可以，保留栈顶不变

        return len(stack)