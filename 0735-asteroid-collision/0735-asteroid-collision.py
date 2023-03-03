class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def one_stack_step(arr):
            stack = []
            for i in arr:
                if not stack:
                    stack.append(i)
                else:
                    if i/abs(i) == stack[-1]/abs(stack[-1]):
                        stack.append(i)
                    else:
                        if i < 0:
                            if abs(i) == abs(stack[-1]):
                                stack.pop()
                            elif abs(i) > abs(stack[-1]):
                                stack.pop()
                                stack.append(i)
                            else:
                                continue
                        else:
                            stack.append(i)
            return stack

        while asteroids:
            new_asteroids = one_stack_step(asteroids)
            if new_asteroids == asteroids:
                break
            else:
                asteroids = new_asteroids
        return asteroids
