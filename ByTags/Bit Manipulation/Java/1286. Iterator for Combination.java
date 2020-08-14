class CombinationIterator {
    int bitmask, n, k;
    String str;

    public CombinationIterator(String characters, int combinationLength) {
        n = characters.length();
        k = combinationLength;
        str = characters;

        bitmask = (1 << n) - (1 << n - k);
    }

    public String next() {
        StringBuilder curr = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if ((bitmask & (1 << n - i - 1)) != 0) {
                curr.append(chars.charAt(i));
            }
        }
        bitmask--;
        while (bitmask > 0 && Integer.bitCount(bitmask) != k) {
            bitmask--;
        }

        return curr.toString();
    }

    public boolean hasNext() {
        return bitmask > 0;
    }
}