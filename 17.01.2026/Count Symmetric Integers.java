class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int count = 0;
        for(int i = low; i <= high; i++){
            int totalDigits = (int)(Math.log10(i)) + 1;
            if(totalDigits % 2 == 0){
                int[] helper = sumOfDigits(i, totalDigits);
                if(helper[0] == helper[1]){
                    count++;
                }
            }
        }
        return count;
    }

    int[] sumOfDigits(int n, int d){
        int sumLeft = 0;
        int sumRight = 0;

        for(int i = 0; i < d/2; i++){
            sumRight += n%10;
            n /= 10;
        }

        for(int i = 0; i < d/2; i++){
            sumLeft += n%10;
            n /= 10;
        }
        return new int[] {sumLeft, sumRight};
    }
}
