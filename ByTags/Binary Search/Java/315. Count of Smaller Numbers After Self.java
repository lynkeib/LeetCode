class Item {
    public int index;
    public int value;
    public int counter;

    public Item(int index, int value, int counter){
        this.index = index;
        this.value = value;
        this.counter = counter;
    }
}

class Solution {
    public List<Integer> countSmaller(int[] nums) {
        List<Item> list = new ArrayList<Item>();
        for(int i = 0; i < nums.length; i++){
            Item item = new Item(i, nums[i], 0);
            list.add(item);
        }
        list = divide(list);
        int[] res = new int[nums.length];
        for(Item item : list){
            int index = item.index;
            int counter = item.counter;
            res[index] = counter;
        }
        List<Integer> resL = new ArrayList<Integer>();
        for(Integer counter : res){
            resL.add(counter);
        }
        return resL;
    }

    public List<Item> divide(List<Item> list){
        int Length = list.size();
        if(Length <= 1){
            return list;
        }
        int endIndex = Length / 2;
        List<Item> list1 = list.subList(0, endIndex);
        List<Item> list2 = list.subList(endIndex, Length);
        list1 = divide(list1);
        list2 = divide(list2);
        List<Item> resList = merge(list1, list2);
        return resList;
    }

    public List<Item> merge(List<Item> list1, List<Item> list2){
        List<Item> resList = new ArrayList<Item>();
        int index1 = 0, index2 = 0;
        while(index1 < list1.size() && index2 < list2.size()){
            Item item1 = list1.get(index1);
            Item item2 = list2.get(index2);
            if(item1.value > item2.value){
                resList.add(item2);
                index2++;
            }else{
                item1.counter += index2;
                resList.add(item1);
                index1++;
            }
        }
        while(index1 < list1.size()){
            Item item1 = list1.get(index1);
            item1.counter += index2;
            resList.add(item1);
            index1++;
        }
        while(index2 < list2.size()){
            Item item2 = list2.get(index2);
            resList.add(item2);
            index2++;
        }
        return resList;
    }
}