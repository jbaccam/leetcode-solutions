class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = nums.length; 
        int[] array = new int[length * 2]; // create an array 2x the length of the array nums
        // iterate over the array
        for (int i = 0; i < length; i++) {
            array[i] = nums[i]; //fills the new array with the old 
            array[i + length] = nums[i]; //duplicates it 
        }
        return array;
    }
}