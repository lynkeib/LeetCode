class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] res = new int[num_people];
        int n = 1;
        int index = 0;
        while(candies > 0){
            int give = Math.min(candies, n);
            candies -= give;
            res[index] += give;
            n += 1;
            index += 1;
            index = index % num_people;
        }
        return res;
    }
}