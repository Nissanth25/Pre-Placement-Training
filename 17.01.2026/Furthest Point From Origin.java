class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        int sp=0;
        int r=0;
        int l=0;
        for(int i=0;i<moves.length();i++){
            if(moves.charAt(i)=='L') l++;
            else if(moves.charAt(i)=='R') r++;
            else sp++;
        }

        int a=Math.abs(sp+r-l);
        int b=Math.abs(sp+l-r);

        if(a>b){
            return a;
        }
        return b;
    }
}
