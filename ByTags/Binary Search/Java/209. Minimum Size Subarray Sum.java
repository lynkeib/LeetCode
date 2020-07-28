class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int slow = 0;
        int sum = 0;
        int res = Integer.MAX_VALUE;
        int[] sums = new int[nums.length + 1];
        for(int i = 0; i < nums.length; i++){
            sums[i + 1] = sums[i] + nums[i];
        }
        for(int i = 0; i < sums.length; i++){
            int target = sums[i] + s;
            int index = biset_left(sums, target);
            if(index != sums.length){
                res = Math.min(res, index - i);
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }

    public int biset_left(int[] sums, int target){
        int left = 0, right = sums.length - 1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(sums[mid] == target){
                return mid;
            }
            if(sums[mid] < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return left;
    }
}