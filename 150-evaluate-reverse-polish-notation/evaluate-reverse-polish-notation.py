class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                # when you push numbers onto the stack, the last number pushed ends up on top,
                # so when you pop them, they come off in reverse order.
                # so like if we have 3 4 -
                # stack would be 
                # 4
                # 3
                # so a = 4 and b = 3
                # but 4 - 3 isnt right, we want 3 - 4, which is b - a
                a, b = stack.pop(), stack.pop() # a is popped first, b is popped second
                # so we want to take a - b
                stack.append(b - a)
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                a, b = stack.pop(), stack.pop() 
                stack.append(int(b / a)) # need to type cast to int because we want to round to zero
            else:
                stack.append(int(i)) # want ints not chars
        return stack[0]