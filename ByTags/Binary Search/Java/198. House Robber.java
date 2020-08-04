class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        if(N == 0){
            return 0;
        }
        int dp0_0 = 0;
        int dp0_1 = Integer.MIN_VALUE;
        for(int i = 0; i < N; i++){
            int temp = dp0_0;
            dp0_0 = Math.max(dp0_1, dp0_0);
            dp0_1 = temp + nums[i];
        }
        return Math.max(dp0_0, dp0_1);
    }
}