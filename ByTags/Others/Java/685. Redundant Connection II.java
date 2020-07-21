class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int N = edges.length;
        int[] inDegree = new int[N];
        int[] res = new int[2];
        int hasTwoInDegree = -1;
        for(int[] e : edges){
            int p = e[0] - 1;
            int n = e[1] - 1;
            inDegree[n]++;
            if(inDegree[n] == 2){
                hasTwoInDegree = n;
                break;
            }
        }
        if(hasTwoInDegree == -1){
            return detectCycle(N, edges, null);
        }else{
            for(int i = N - 1; i > -1; i--){
                int[] e = edges[i];
                int n1 = e[0] - 1, n2 = e[1] - 1;
                if(n2 == hasTwoInDegree){
                    int[] Cycle = detectCycle(N, edges, e);
                    if(Cycle == null){
                        return e;
                    }
                }
            }
        }
        return res;
    }

    public int[] detectCycle(int N, int[][] edges, int[] skipEdge){
        int[] roots = new int[N];
        for(int i = 0; i < N; i++){
            roots[i] = i;
        }
        for(int[] e : edges){
            if(Arrays.equals(e, skipEdge)){
                continue;
            }
            else{
                int n1 = e[0] - 1;
                int n2 = e[1] - 1;
                int p1 = find(roots, n1), p2 = find(roots, n2);
                if(p1 == p2){
                    return e;
                }else{
                   roots[p2] = p1;
                }
            }
        }
        return null;
    }

    public int find(int[] roots, int node){
        if(roots[node] != node){
            roots[node] = find(roots, roots[node]);
        }
        return roots[node];
    }
}