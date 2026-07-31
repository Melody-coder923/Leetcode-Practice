class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        int len = getLen(low);
        List<Integer> ans = new ArrayList();
        
        for (int i = len; i <= 9; i++) {
            for (int j = 1; j <= 9-i+1; j++) {
                int num = getNum(j, i);
                if (num <= high && num >= low) {
                    ans.add(num);
                }
            }
        }

        return ans;
    }
    
    private int getNum(int lead, int len) {
        int ret = 0;
        
        for (int i = 0; i < len; i++) {
            ret = ret * 10 + lead + i;
        }
        
        return ret;
    }

    private int getLen(int num) {
        int cur = num;
        int ret = 0;

        while (cur > 0) {
            cur = cur / 10;
            ret++;
        }
        
        return ret;
    }
}