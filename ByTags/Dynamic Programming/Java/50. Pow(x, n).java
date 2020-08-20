class Solution {

    Map<Long, Double> dp = new HashMap();

    public double myPow(double x, int n) {
        long nn = n;
        if(nn < 0){
            x = 1 / x;
            nn = -nn;
        }
        dp.put((long)0, 1.0);
        dp.put((long)1, x);
        return dfs(nn);
    }

    public double dfs(long n){
        if(dp.containsKey(n)){
            return dp.get(n);
        }
        double thisNum = dfs(n / 2) * dfs(n - n / 2);
        dp.put(n, thisNum);
        return thisNum;
    }
}