class Solution {
    public List<String> readBinaryWatch(int num) {
        List<String> res = new ArrayList<>();
        for(int hour = 0; hour < 12; hour++){
            for(int minute = 0; minute < 60; minute++){
                long hourCount = count(hour);
                long minuteCount = count(minute);
                if(hourCount + minuteCount == num){
                    String sbuf = String.format("%d:%02d", hour, minute);
                    res.add(sbuf.toString());
                }
            }
        }
        return res;
    }

    public long count(int num){
        String binary = Integer.toBinaryString(num);
        long count = binary.chars().filter(ch -> ch == '1').count();
        return count;
    }
}