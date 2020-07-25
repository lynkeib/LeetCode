class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
        dict.put(0, -1);
        int sum = 0, res = 0;
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            int target = sum - k;
            if(dict.containsKey(target)){
                res = Math.max(res, i - dict.get(target));
            }
            if(!dict.containsKey(sum)){
                dict.put(sum, i);
            }
        }
        return res;
    }
}