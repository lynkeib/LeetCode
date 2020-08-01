class Solution {
    public int findMaximumXOR(int[] nums) {
        int max = 0;
        for(int num: nums){
            max = Math.max(max, num);
        }
        String binaryMax = Integer.toBinaryString(max);
        int maxLength = binaryMax.length();
        int res = 0;
        for(int leftMove = maxLength - 1; leftMove > -1; leftMove--){
            res <<= 1;
            int thisTry = res | 1;
            Set<Integer> prefix = new HashSet<>();
            for(int num : nums){
                prefix.add(num >> leftMove);
            }
            for(int p : prefix){
                int target = thisTry ^ p;
                if(prefix.contains(target)){
                    res = thisTry;
                    break;
                }
            }
        }return res;
    }
}