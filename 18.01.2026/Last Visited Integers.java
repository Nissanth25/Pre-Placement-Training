class Solution {
    public List<Integer> lastVisitedIntegers(int[] nums) {
        List<Integer> lis = new LinkedList<Integer>();
        int count = 0;
        List<Integer> seen = new ArrayList<Integer>();
        for(int i =0;i<nums.length;i++){
            if(nums[i]!=-1){
                seen.add(nums[i]);
                count = seen.size();
            }
            else if(count==0){
                lis.add(-1);
            }
            else{
                lis.add(seen.get(--count));
            }
        }
        return lis;
    }
}
