class Solution:
    def calculate(self, s: str) -> int:
        current_number = 0
        operation = '+'
        s+='+'
        stack = []
        for char in s:
            if char.isdigit():
                current_number = current_number*10 + (ord(char)-ord('0'))
            elif char == ' ':
                    pass
            else:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    stack.append((stack.pop()*current_number))
                elif operation == '/':
                    stack.append(math.trunc(stack.pop()/current_number))
                current_number = 0
                operation = char
        return sum(stack)
        