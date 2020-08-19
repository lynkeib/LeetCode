class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        var counter = new HashMap<Character, Integer>();
        for(char c : p.toCharArray()){
            var num = counter.getOrDefault(c, 0);
            counter.put(c, num + 1);
        }
        var tempCounter = new HashMap<Character, Integer>();
        for(char c : counter.keySet()){
            tempCounter.put(c, counter.get(c));
        }
        var count = counter.size();
        var res = new ArrayList<Integer>();
        int slow = 0;
        for(int fast = 0; fast < s.length(); fast++){
            char thisC = s.charAt(fast);
            if(!counter.containsKey(thisC)){
                slow = fast + 1;
                for(char c : counter.keySet()){
                    tempCounter.put(c, counter.get(c));
                }
                count = counter.size();
            }else{
                var fastCount = tempCounter.get(thisC);
                fastCount--;
                if(fastCount == 0){
                    count--;
                }
                tempCounter.put(thisC, fastCount);
                while(slow < fast && tempCounter.get(thisC) < 0){
                    var slowC = s.charAt(slow);
                    var slowCount = tempCounter.get(slowC);
                    if(slowCount == 0){
                        count++;
                    }
                    slowCount++;
                    tempCounter.put(slowC, slowCount);
                    slow++;
                }
                if(count == 0){
                    res.add(slow);
                }
            }
        }
        return res;
    }
}