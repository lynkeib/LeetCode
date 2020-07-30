class Solution {
    public int compress(char[] chars) {
        int slow = 0, fast = 0;
        while(fast < chars.length){
            char thisC = chars[fast];
            chars[slow] = thisC;
            int counter = 0;
            while(fast < chars.length && chars[fast] == thisC){
                counter++;
                fast++;
            }
            if(fast == chars.length){
                if(counter == 1){
                    return slow + 1;
                }else{
                    slow++;
                    String str = String.valueOf(counter);
                    for(char n : str.toCharArray()){
                        chars[slow] = n;
                        slow++;
                    }
                    return slow;
                }
            }
            if(counter == 1){
                slow++;
            }else{
                slow++;
                String str = String.valueOf(counter);
                for(char n : str.toCharArray()){
                    chars[slow] = n;
                    slow++;
                }
            }
        }
        return slow;
    }
}