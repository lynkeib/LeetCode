class Solution {
    public int characterReplacement(String s, int k) {
        int slow = 0;
        int res = 0;
        int[] counter = new int[26];
        int maxCount = 0;
        for(int fast = 0; fast < s.length(); fast++){
            counter[s.charAt(fast) - 'A']++;
            maxCount = Math.max(maxCount, counter[s.charAt(fast) - 'A']);
            while(fast - slow + 1 - maxCount > k){
                counter[s.charAt(slow) - 'A']--;
                slow++;
            }
            res = Math.max(res, fast - slow + 1);
        }
        return res;
    }
}