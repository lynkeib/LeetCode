class Solution {
    public int largestRectangleArea(int[] heights) {
        int res = 0;
        var stack = new Stack<Integer>();
        stack.push(-1);
        for(int i = 0; i < heights.length; i++){
            while(stack.peek() != -1 && heights[stack.peek()] > heights[i]){
                var popIndex = stack.pop();
                var popHeight = heights[popIndex];
                var leftIndex = stack.peek();
                var Width = i - leftIndex - 1;
                res = Math.max(res, Width * popHeight);
            }
            stack.push(i);
        }
        while(stack.peek() != -1){
            var popIndex = stack.pop();
            var popHeight = heights[popIndex];
            var leftIndex = stack.peek();
            var Width = heights.length - leftIndex - 1;
            res = Math.max(res, Width * popHeight);
        }
        return res;
    }
}