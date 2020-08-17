class Solution {
    public int maxProfit(int[] prices) {
        int K = 2;
        int days = prices.length;
        int[][][] dp = new int[days + 1][2][K + 1];
        for(int i = 0; i < days; i++){
            dp[i][0][0] = 0;
            dp[i][1][0] = Integer.MIN_VALUE;
        }
        for(int k = 0; k <= K; k++){
            dp[0][0][k] = 0;
            dp[0][1][k] = Integer.MIN_VALUE;
        }
        for(int day = 1; day <= days; day++){
            for(int k = 1; k <= K; k++){
                dp[day][0][k] = Math.max(dp[day - 1][0][k], dp[day - 1][1][k] + prices[day - 1]);
                dp[day][1][k] = Math.max(dp[day - 1][1][k], dp[day - 1][0][k - 1] - prices[day - 1]);
            }
        }
        int res = Integer.MIN_VALUE;
        for(int k = 0; k <= K; k++){
            res = Math.max(res, dp[days][0][k]);
        }
        return res;
    }
}