class Solution {
    public boolean isValid(String s) {
        if(s.length() == 0){
            return true;
        }
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            // checks if it starts with these characters, cause if it doesnt then its already out of order
            if (current == '(' || current == '[' || current == '{') {
                stack.push(current);
            } else {
                // stack cant be empty
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop(); // we have to pop so that for the next iterations it doesnt intefer
                if ((current == ')' && top != '(' )|| 
                    (current == '}' && top != '{' )||
                    (current == ']' && top != '[')) {
                        return false;
                    }
            }
        }
        return stack.isEmpty();
    }
}