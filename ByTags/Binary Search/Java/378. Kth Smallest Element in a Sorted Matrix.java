class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int left = matrix[0][0], right = matrix[n - 1][n - 1];
        while(left < right){
            int mid = left + (right - left) / 2;
            int[] res = find(matrix, mid);
            int count = res[0], smaller = res[1], larger = res[2];
            if(count == k){
                return smaller;
            }
            if(count > k){
                right = smaller;
            }else{
                left = larger;
            }
        }
        return left;
    }

    public int[] find(int[][] matrix, int target){
        int n = matrix.length;
        int row = n - 1, col = 0;
        int smaller = matrix[0][0], larger = matrix[n - 1][n - 1];
        int[] res = new int[3]; //[K, row, col]
        int count = 0;
        while(row > -1 && col < n){
            int num = matrix[row][col];
            if(target >= num){
                count += row + 1;
                smaller = Math.max(smaller, num);
                col++;
            }else{
                larger = Math.min(larger, num);
                row--;
            }
        }
        res[0] = count;
        res[1] = smaller;
        res[2] = larger;
        return res;
    }
}