class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        keys_ = list(string.ascii_lowercase)
        values_ = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = dict(list(zip(keys_, values_)))
        result_set = set()
        for word in words:
            translation = ''
            for l in word:
                translation += d[l]
            result_set.add(translation)
        return len(result_set)
