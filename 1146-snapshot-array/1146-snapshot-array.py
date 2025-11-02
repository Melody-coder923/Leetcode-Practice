class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [ [( -1, 0 )] for _ in range(length) ]  # 每个索引的修改记录，初始值为 0

    def set(self, index: int, val: int) -> None:
        # 记录当前 snap_id 下的值
        if self.data[index][-1][0] == self.snap_id:
            # 如果当前 snap_id 已经有修改，覆盖旧值
            self.data[index][-1] = (self.snap_id, val)
        else:
            self.data[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.data[index]
        # 调用自定义二分查找
        return self.binary_search(arr, snap_id)

    def binary_search(self, arr, snap_id):
        left, right = 0, len(arr) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return arr[res][1]
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)