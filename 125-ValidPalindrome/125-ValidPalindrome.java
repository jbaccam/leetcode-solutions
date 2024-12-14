class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder string = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                string.append(Character.toLowerCase(c));
            }
        }
        return string.toString().equals(string.reverse().toString());
    }
}