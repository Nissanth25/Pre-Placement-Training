class Solution {
    public int minimumRightShifts(List<Integer> ls) {
        int n=ls.size();
        int count=0;
        List<Integer> copy=new ArrayList<>(ls);
        Collections.sort(copy);
        if(ls.equals(copy)){
            return 0;
        }
        while(count<n){
            int num=ls.remove(n-1);
            ls.add(0,num);
            int flag=1;
            for(int i=0;i<n;i++){
                if(ls.get(i)!=copy.get(i)){
                    flag=0;
                    break;
                }
            }
            count++;
            if(flag==1){
                return count;
            }
        }
        return -1;
    }
}
