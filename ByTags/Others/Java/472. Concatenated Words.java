class Solution {

    Set<String> visited;

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        visited = new HashSet<>(Arrays.asList(words));
        List<String> res = new ArrayList<String>();
        for(String word : words){
            if(dfs(word)){
                res.add(word);
            }
        }
        return res;
    }

    public boolean dfs(String word){
        for(int i = 1; i < word.length(); i++){
            String pre = word.substring(0, i);
            if(visited.contains(pre)){
                String suf = word.substring(i);
                if(visited.contains(suf) || dfs(suf)){
                    visited.add(suf);
                    return true;
                }
            }
        }
        return false;
    }
}