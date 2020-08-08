class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        Deque deque = new LinkedList();
        int index = 0;
        while(index < intervals.length){
            if(deque.size() == 0){
                deque.addLast(intervals[index]);
            }else{
                int[] pop = (int[])deque.pollLast();
                if(pop[1] >= intervals[index][0]){
                    deque.addLast(new int[]{Math.min(pop[0], intervals[index][0]), Math.max(pop[1], intervals[index][1])});

                }else{
                    deque.addLast(pop);
                    deque.addLast(intervals[index]);
                }
            }
            index++;
        }
        int[][] res = new int[deque.size()][2];
        index = 0;
        while(deque.size() != 0){
            res[index] = (int[]) deque.pollFirst();
            index++;
        }
        return res;
    }
}