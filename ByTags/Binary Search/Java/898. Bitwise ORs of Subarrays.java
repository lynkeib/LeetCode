class Solution {
    public int subarrayBitwiseORs(int[] A) {
        Set<Integer> res = new HashSet();
        Set<Integer> curr = new HashSet();
        curr.add(0);
        for(int num : A){
            Set<Integer> thisCurr = new HashSet();
            for(int n : curr){
                thisCurr.add(num | n);
            }
            thisCurr.add(num);
            curr = thisCurr;
            res.addAll(curr);
        }
        return res.size();
    }
}