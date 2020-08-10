class Pair{
    int x, y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}
class Solution {

    int[] dirs = new int[]{-1, 0, 1, 0, -1};

    public int trapRainWater(int[][] heightMap) {
        int rows = heightMap.length;
        if(rows == 0){
            return 0;
        }
        int cols = heightMap[0].length;
        var peakHeight = new int[rows][cols];
        for(int row = 0; row < rows; row++){
            Arrays.fill(peakHeight[row], Integer.MAX_VALUE);
        }
        var queue = new LinkedList<Pair>();
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
                if(row == 0 || row == rows - 1 || col == 0 || col == cols - 1){
                    peakHeight[row][col] = heightMap[row][col];
                    queue.addLast(new Pair(row, col));
                }
            }
        }
        while(queue.size() != 0){
            var pop = queue.pollFirst();
            for(int i = 0; i < 4; i++){
                int nx = pop.x + dirs[i], ny = pop.y + dirs[i + 1];
                if(nx > 0 && nx < rows - 1 && ny > 0 && ny < cols - 1){
                    int limit = Math.max(peakHeight[pop.x][pop.y], heightMap[nx][ny]);
                    if(peakHeight[nx][ny] > limit){
                        peakHeight[nx][ny] = limit;
                        queue.addLast(new Pair(nx, ny));
                    }
                }
            }
        }
        int res = 0;
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
                res += peakHeight[row][col] - heightMap[row][col];
            }
        }
        return res;
    }
}