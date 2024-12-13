class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> result = new HashMap<>();
        for (String s : strs) {
            int[] count = new int[26]; // count[0] corresponds to 'a', count[1] corresponds to 'b', etc
            for (char c : s.toCharArray()) { // iterate over every character in the string, s.toCharArray() converts the string s into an array of characters.
                count[c - 'a']++; // increase the count for whatever character it finds
                // subtracting 'a' from c gives the index of the character in the alphabet, a is represented as a unicode integer value
            }
            String key = Arrays.toString(count); // convert the array back to a string
            // if this is the first time we're encountering this key (specific set of characters), create a new list and associate it with the key
            // if the key already exists, no new list will be created because it means we've already started a grouping for the key
            result.putIfAbsent(key, new ArrayList<>()); 
            // retrieves the list associated with the current key from the map and adds the string to the list
            result.get(key).add(s); // retrieve the value associated with the key (key is the string, value is the arraylist), then add to the arraylist
        }
        return new ArrayList<>(result.values());
    }
}