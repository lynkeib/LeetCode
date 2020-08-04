class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        if(N == 0){
            return 0;
        }
        int dp0_0 = nums[0], dp0_1 = nums[0];
        int Cdp0_0 = 0, Cdp0_1 = 0;
        for(int i = 1; i < N - 1; i++){
            int temp = dp0_0;
            if(i == 1){
                dp0_0 = dp0_1;
                dp0_1 = Math.max(temp + 0, dp0_1);
            }else{
                dp0_0 = dp0_1;
                dp0_1 = Math.max(temp + nums[i], dp0_1);
            }
            temp = Cdp0_0;
            Cdp0_0 = Cdp0_1;
            Cdp0_1 = Math.max(temp + nums[i], Cdp0_1);
        }
        Cdp0_1 = Math.max(Cdp0_1, Cdp0_0 + nums[N - 1]);
        return Math.max(Cdp0_1, dp0_1);
    }
}