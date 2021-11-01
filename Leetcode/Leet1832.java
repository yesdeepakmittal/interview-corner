class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] arr = new boolean[26];
        int alpha;
        
        sentence = sentence.toLowerCase();
        
        for(int i = 0; i< sentence.length(); i++){
            alpha = sentence.charAt(i) - 'a';
            arr[alpha] = true; //index of each alphabet from 0(for a) to 25(for z)
        }
        
        for(int i = 0; i < 26; i++){
            if(!arr[i]){
                return false;
            }
        } return true;
    }
}