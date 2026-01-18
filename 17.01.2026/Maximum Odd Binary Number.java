class Solution {
    public String maximumOddBinaryNumber(String s) {
        int n=s.length();
        int count=0;
        StringBuilder sb=new StringBuilder();
        for(char ch:s.toCharArray()){
            if(ch=='1') count++;
        }
        for(int i=0;i<count-1;i++){
            sb.append(1);
        }
        for(int i=0;i<(s.length()-count);i++){
            sb.append(0);
        }
        sb.append(1);
        return sb.toString();

    }
}
