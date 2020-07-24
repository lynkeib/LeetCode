class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] counter = new int[128];
        int slow = 0, res = 0;
        for(int fast = 0; fast < s.length(); fast++){
            char thisChar = s.charAt(fast);
            counter[thisChar]++;
            while(counter[s.charAt(fast)] > 1){
                char charAtSlow = s.charAt(slow);
                counter[charAtSlow]--;
                slow++;
            }
            res = Math.max(res, fast - slow + 1);
        }
        return res;
    }
}