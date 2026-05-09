public int lengthOfLIS(int[] nums) {
    int N = nums.length, dp[] = new int[N], res = 1;
    Arrays.fill(dp, 1);
    for (int i = 1; i < N; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        res = Math.max(res, dp[i]);
    }
    return res;
}