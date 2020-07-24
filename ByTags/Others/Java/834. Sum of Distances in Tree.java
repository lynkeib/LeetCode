class Solution {

    int[] res, count;
    List<Set<Integer>> graph;
    int N;

    public int[] sumOfDistancesInTree(int N, int[][] edges) {
        this.N = N;
        graph = new ArrayList<Set<Integer>>();
        res = new int[N];
        count = new int[N];
        Arrays.fill(count, 1);

        for(int i = 0; i < N; i++){
            graph.add(new HashSet<Integer>());
        }

        for(int[] edge : edges){
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        CountNode(0, -1);
        CountParent(0, -1);
        return res;
    }

    public void CountNode(int node, int parent){
        for(int child : graph.get(node)){
            if(child != parent){
                CountNode(child, node);
                count[node] += count[child];
                res[node] += res[child] + count[child];
            }
        }
    }

    public void CountParent(int node, int parent){
        for(int child : graph.get(node)){
            if(child != parent){
                res[child] = res[node] - count[child] + (N - count[child]);
                CountParent(child, node);
            }
        }
    }
}