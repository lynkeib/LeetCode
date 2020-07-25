class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
        int res = 0, subset = 0, slow = 0;
        for(int fast = 0; fast < A.length; fast++){
            int num = A[fast];
            if(!counter.containsKey(num)){
                counter.put(num, 0);
            }
            counter.put(num, counter.get(num) + 1);
            while(counter.get(A[slow]) > 1 || counter.size() > K){
                if(counter.get(A[slow]) > 1){
                    subset++;
                    counter.put(A[slow], counter.get(A[slow]) - 1);
                }else{
                    counter.put(A[slow], counter.get(A[slow]) - 1);
                    if(counter.get(A[slow]) == 0){
                        counter.remove(A[slow]);
                    }
                    subset = 0;
                }
                slow++;
            }
            if(counter.size() == K){
                res += subset + 1;
            }
        }
        return res;

    }
}