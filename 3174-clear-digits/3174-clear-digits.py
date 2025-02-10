class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for character in s:
            if character.isalpha():
                stack.append(character)
            elif character.isdigit():
                stack.pop()
        return "".join(stack)
            