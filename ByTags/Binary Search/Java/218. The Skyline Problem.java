class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> res = new ArrayList<>();
        List<int[]> buildingsLine = new ArrayList<>();
        for(int[] lines : buildings){
            buildingsLine.add(new int[]{lines[0], -lines[2]});
            buildingsLine.add(new int[]{lines[1], lines[2]});
        }
        Collections.sort(buildingsLine, (a, b)->{
            if(a[0] != b[0]) return a[0] - b[0];
            else return a[1] - b[1];
        });
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> b - a);
        heap.add(0);
        int preHeight = 0;
        for(int[] point : buildingsLine){
            int x = point[0], y = point[1];
            if(y < 0) heap.add(-y);
            else heap.remove(y);
            if(heap.peek() != preHeight){
                res.add(Arrays.asList(x, heap.peek()));
                preHeight = heap.peek();
            }
        }
        return res;
    }
}