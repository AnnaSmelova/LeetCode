class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        last_int = 0
        for char in s:
            if char.isnumeric():
                if arr and last_int:
                    last_char = arr.pop()
                    last_char += char
                    arr.append(last_char)
                else:
                    arr.append(char)
                last_int = 1
            elif char == ' ':
                continue
            else:
                arr.append(char)
                last_int = 0
        stack = []
        i = 0
        while i < len(arr):
            if arr[i].isnumeric():
                stack.append(arr[i])
                i += 1
            else:
                if arr[i] == '*':
                    last_num = int(stack.pop())
                    res = last_num * int(arr[i + 1])
                    stack.append(str(res))
                elif arr[i] == '/':
                    last_num = int(stack.pop())
                    if last_num >= 0 and int(arr[i + 1]) >= 0:
                        res = last_num // int(arr[i + 1])
                    else:
                        res = (-1) * (abs(last_num) // abs(int(arr[i + 1])))
                    stack.append(str(res))
                elif arr[i] == '+':
                    stack.append(arr[i + 1])
                else:
                    stack.append('-' + arr[i + 1])
                i += 2
        return sum(list(map(int, stack)))
        