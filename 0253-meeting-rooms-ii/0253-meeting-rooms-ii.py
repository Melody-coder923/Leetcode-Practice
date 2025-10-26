class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))    # 1表示开始
            events.append((end, -1))     # -1表示结束
        events.sort()
        rooms = 0
        max_rooms = 0
        for time, delta in events:
            rooms += delta
            max_rooms = max(rooms, max_rooms)
        return max_rooms