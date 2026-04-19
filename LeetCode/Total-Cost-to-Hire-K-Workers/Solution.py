def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    from collections import deque

    left_queue = costs[:candidates]
    remaining_workers = deque(costs[candidates:-candidates])
    right_queue = costs[max(candidates, len(costs)-candidates):]

    heapify(left_queue)
    heapify(right_queue)

    costs = 0
    for i in range(k):
        # Make sure that the left_queue is not exhausted
        # Now, if the right_queue is exhausted, we can just pop from left
        # <= ensures the ties are broken by taking left
        if left_queue and (not right_queue or left_queue[0] <= right_queue[0]):
            costs += heappop(left_queue)
            if remaining_workers:
                heappush(left_queue, remaining_workers.popleft())
        else:
            costs += heappop(right_queue)
            if remaining_workers:
                heappush(right_queue, remaining_workers.pop())

    return costs