class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> res = new ArrayList<>();
        Map<String, Integer> visited = new HashMap<>();
        for(int i = 0; i <= s.length() - 10; i++){
            String thisString = s.substring(i, i+10);
            visited.put(thisString, visited.getOrDefault(thisString, 0) + 1);
            if(visited.containsKey(thisString) && visited.get(thisString) == 2){
                res.add(thisString);
            }
        }
        return res;
    }
}

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> res = new ArrayList<>();
        if(s.length() <= 10){
            return res;
        }

        Map<Character, Integer> map = new HashMap<>(){{put('A', 0); put('C', 1); put('G', 2); put('T', 3);}};

        Map<Integer, Integer> visited = new HashMap<>();

        int base = 4, hash = 0, highest = (int)Math.pow(base, 10);
        for(int i = 0; i < 10; i++){
            char thisChar = s.charAt(i);
            int thisNum = map.get(thisChar);
            hash = hash * base + thisNum;
        }
        visited.put(hash, 1);
        for(int i = 10; i < s.length(); i++){
            char thisChar = s.charAt(i);
            int thisNum = map.get(thisChar);
            char lastChar = s.charAt(i - 10);
            int lastNum = map.get(lastChar);
            hash = hash * base - lastNum * highest + thisNum;
            visited.put(hash, visited.getOrDefault(hash, 0) + 1);
            if(visited.get(hash) == 2){
                res.add(s.substring(i - 9, i + 1));
            }
        }
        return res;
    }
}