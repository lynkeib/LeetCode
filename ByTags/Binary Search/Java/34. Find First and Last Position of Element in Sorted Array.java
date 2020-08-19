class Solution {
    public int[] searchRange(int[] nums, int target) {
        var res = new int[2];
        res[0] = -1;
        res[1] = -1;
        if(nums.length == 0){
            return res;
        }
        res[0] = findLeft(nums, target);
        res[1] = findRight(nums, target);
        return res;
    }

    public int findLeft(int[] nums, int target){
        int left = 0, right = nums.length - 1;
        while(left < right){
            int mid = left + (right - left) / 2;
            if(nums[mid] < target){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        if(left > right || nums[left] != target){
            return -1;
        }
        return left;
    }

    public int findRight(int[] nums, int target){
        int left = 0, right = nums.length - 1;
        while(left < right){
            int mid = left + (right - left) / 2 + 1;
            if(nums[mid] <= target){
                left = mid;
            }else{
                right = mid - 1;
            }
        }
        if(left > right || nums[left] != target){
            return -1;
        }
        return left;
    }
}