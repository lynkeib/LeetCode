class Solution {

    boolean error = false;
    Map<Character, Set<Character>> graph = new HashMap<>();
    int[] Indegree = new int[26];

    public String alienOrder(String[] words) {
        buildGraph(words);
        if(error){
            return "";
        }
        var res = bfs();
        return res;
    }

    public String bfs(){
        Queue<Character> queue = new LinkedList<>();
        for(int i = 0; i < 26; i++){
            char c = (char)(i + (int)'a');
            if(Indegree[i] == 0 && graph.containsKey(c)){
                queue.offer(c);
            }
        }
        int totalLetters = graph.keySet().size();
        StringBuilder sb = new StringBuilder();
        while(queue.size() != 0){
            char c = queue.poll();
            sb.append(c);
            for(char nei : graph.get(c)){
                Indegree[nei - 'a']--;
                if(Indegree[nei - 'a'] == 0){
                    queue.offer(nei);
                }
            }
        }
        if(sb.length() != totalLetters){
            return "";
        }
        return sb.toString();
    }

    public void buildGraph(String[] words){
        for(String word : words){
            for(char c : word.toCharArray()){
                if(!graph.containsKey(c)){
                    graph.put(c, new HashSet<Character>());
                }
            }
        }
        for(int i = 0; i < words.length - 1; i++){
            String word1 = words[i], word2 = words[i + 1];
            int minLength = Math.min(word1.length(), word2.length());
            for(int j = 0; j < minLength; j++){
                if(word1.charAt(j) != word2.charAt(j)){
                    char in = word2.charAt(j), out = word1.charAt(j);
                    if(!graph.get(out).contains(in)){
                        Set<Character> temp = graph.get(out);
                        temp.add(in);
                        graph.put(out, temp);
                        Indegree[in - 'a']++;
                    }
                    break;
                }
                if(j == minLength - 1 && word1.length() > word2.length()){
                    error = true;
                }
            }
        }
    }
}