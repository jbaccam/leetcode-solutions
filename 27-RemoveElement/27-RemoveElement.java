class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // Pointer to track the position of elements not equal to val
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            // If the current element is not equal to val, copy it to the position at k and increment k
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        
        // Return the new length of the array
        return k;
    }
}
