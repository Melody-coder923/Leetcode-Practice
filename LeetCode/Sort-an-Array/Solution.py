    private void merge(int[] nums, int low, int mid, int high, int[] temp) {
        for(int i = low; i <= mid; i++) {
            temp[i] = nums[i];
        }

        for(int i = mid + 1; i <= high; i++) {
            temp[i] = nums[i];
        }

        int i = low, j = mid + 1;
        while(i <= mid && j <= high) {
            if(temp[i] < temp[j]) {
                nums[low++] = temp[i++];
            } else {
                nums[low++] = temp[j++];
            }
        }

        while(i <= mid) {
            nums[low++] = temp[i++];
        }

        while(j <= high) {
            nums[low++] = temp[j++];
        }   
    }