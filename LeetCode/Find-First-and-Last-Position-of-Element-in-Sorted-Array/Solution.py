var searchRange = function(nums, target) {
    if (nums.length === 0) return [-1, -1];
    
    function findLeftMostIndex() {
        let left = 0;
        let right = nums.length - 1;
        let leftMostIndex = -1;
        while (left <= right) {
            const mid = Math.trunc((left + right) / 2);
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;    
            } else {
                leftMostIndex = mid;
                right = mid - 1;     
            }
        }
        return leftMostIndex;
    }
    
    function findRightMostIndex() {
        let left = 0;
        let right = nums.length - 1;
        let rightMostIndex = -1;
        
        while (left <= right) {
            const mid = Math.trunc((left + right) / 2);
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                rightMostIndex = mid;
                left = mid + 1;
            }
        }
        return rightMostIndex;
    }
        
    const left = findLeftMostIndex();
    
    if (left === -1) return [-1, -1];
    
    const right = findRightMostIndex();
    
    return [left, right];
};