class Solution {
    public int removeDuplicates(int[] nums) {
        /**
        Some notes:
        In-place
        No sorting required
        Remaining elemetns and size is not important
         */

        
        int i = 0; // this is where we'll place the numbers to update the array in place

        // iterate over the array
        for (int j = 0; j < nums.length; j++) {
            // if the current num is different from the last num
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }

}