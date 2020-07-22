// DP
class Solution {
    public int mctFromLeafValues(int[] arr) {
        int len = arr.length;
        int[][] dp = new int[len][len];
        int[][] max = new int[len][len];

        for(int i = 0; i < len; i++){
            max[i][i] = arr[i];
        }

        for(int length = 1; length < len; length++){
            for(int start = 0; start + length < len; start++){
                int end = start + length;
                max[start][end] = Math.max(max[start][end - 1], arr[end]);
            }
        }

        for(int length = 1; length <= len; length++){
            for(int start = 0; start + length < len; start++){
                int end = start + length;
                int res = Integer.MAX_VALUE;
                for(int k = start; k < end; k++){
                    int thisRes = dp[start][k] + dp[k+1][end] + max[start][k] * max[k+1][end];
                    res = Math.min(res, thisRes);
                }
                dp[start][end] = res;
            }
        }

        // System.out.println(Arrays.deepToString(dp));
        return dp[0][len - 1];
    }
}

// Stack
class Solution {
    public int mctFromLeafValues(int[] arr) {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(Integer.MAX_VALUE);
        Integer res = 0;
        for(Integer num : arr){
            while(num > stack.peek()){
                Integer popNum = stack.pop();
                res += Math.min(num, stack.peek()) * popNum;
            }
            stack.push(num);
        }
        while(stack.size() != 2){
            Integer popNum = stack.pop();
            res += popNum * stack.peek();
        }
        return res;
    }
}