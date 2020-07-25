class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int rows = matrix.length, cols = matrix[0].length;
        int[][] ps = new int[rows + 1][cols + 1];
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
                ps[row + 1][col + 1] = ps[row][col + 1] + ps[row+1][col] - ps[row][col] + matrix[row][col];
            }
        }
        int res = 0;
        Map<Integer, Integer> map = new HashMap();
        for(int row1 = 1; row1 <= rows; row1++){
            for(int row2 = row1; row2 <= rows; row2++){
                map.clear();
                map.put(0, 1);
                for(int col = 1; col <= cols; col++){
                    int currSum = ps[row2][col] - ps[row1 - 1][col];
                    int find = currSum - target;
                    res += map.getOrDefault(find, 0);
                    map.put(currSum, map.getOrDefault(currSum, 0) + 1);
                }
            }
        }
        return res;
    }
}