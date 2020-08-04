class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int topRow = 0, bottomRow = n, leftCol = 0, rightCol = n;
        int curr = 1;
        while(curr <= n * n){
            for(int col = leftCol; col < rightCol; col++){
                res[topRow][col] = curr;
                curr++;
            }
            topRow++;
            for(int row = topRow; row < bottomRow; row++){
                res[row][rightCol - 1] = curr;
                curr++;
            }
            rightCol--;
            for(int col = rightCol -1; col >= leftCol; col--){
                res[bottomRow - 1][col] = curr;
                curr++;
            }
            bottomRow--;
            for(int row = bottomRow - 1; row >= topRow; row--){
                res[row][leftCol] = curr;
                curr++;
            }
            leftCol++;
        }
        return res;
    }
}