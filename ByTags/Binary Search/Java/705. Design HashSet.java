class MyHashSet {

    int[] nums = new int[1000001];

    /** Initialize your data structure here. */
    public MyHashSet() {

    }

    public void add(int key) {
        nums[key] = 1;
        return;
    }

    public void remove(int key) {
        nums[key] = 0;
        return;
    }

    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        return nums[key] == 1;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */