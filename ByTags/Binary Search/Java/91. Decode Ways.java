class Solution {
    public int numDecodings(String s) {
        int N = s.length();
        if(N == 0){
            return 0;
        }
        int dp1D = s.charAt(0) == '0' ? 0 : 1, dp2D = 1;
        for(int i = 1; i < N; i++){
            int thisdp = 0;
            if(s.charAt(i) != '0'){
                thisdp += dp1D;
            }
            if(s.charAt(i - 1) == '1'){
                thisdp += dp2D;
            }else if(s.charAt(i - 1) == '2' && s.charAt(i) <= '6'){
                thisdp += dp2D;
            }
            dp2D = dp1D;
            dp1D = thisdp;
        }
        return dp1D;
    }
}