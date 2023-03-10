class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        d = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'],
            5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'],
            8:['t','u','v'], 9:['w','x','y','z']}

        queue = ['']
        
        for digit in digits:
            digit = int(digit)            
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for letter in d[digit]:
                    queue.append(curr + letter)
        
        return queue
