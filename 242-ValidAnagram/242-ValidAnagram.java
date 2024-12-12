class Solution {
    public boolean isAnagram(String s, String t) {
        // if they arent the same length, instantly false
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> mapS = new HashMap<>();
        HashMap<Character, Integer> mapT = new HashMap<>();
        
        // since they are they same length we can just use the same for loop and int i
        for (int i = 0; i < s.length(); i++) {
            // using getOrDefault we can count how many times each character appears in both strings
            mapS.put(s.charAt(i), mapS.getOrDefault(s.charAt(i), 0) + 1); // default is now 1, and if gets a value that exists, add one
            mapT.put(t.charAt(i), mapT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return mapS.equals(mapT);
    }
}