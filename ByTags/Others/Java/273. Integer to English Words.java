class Solution {

    String[] to20 = new String[]{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    String[] ten = new String[]{"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    String[] unit = new String[]{"Thousand", "Million", "Billion"};

    public String numberToWords(int num) {
        String res = helper(num);
        return res == "" ? "Zero" : res.trim();
    }

    public String helper(int num) {
        if(num == 0){
            return "";
        }
        if(num < 20){
            return to20[num - 1];
        }
        if(num < 100){
            return ten[num/10 - 2] + " " + helper(num % 10).trim();
        }
        if(num < 1000){
            return to20[num/100 - 1] + " Hundred "+ helper(num % 100).trim();
        }
        for(int i = 1; i <= 3; i++){
            double u = Math.pow(1000, i + 1);
            double less = Math.pow(1000, i);
            if(num < u){
                return helper((int)((double)num / less)).trim() + " " + unit[i - 1] + " " + helper((int)((double)num % less)).trim();
            }
        }
        return "";
    }
}