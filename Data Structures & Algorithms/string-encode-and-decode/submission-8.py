class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for string in strs:
            code += str(len(string)) + '#' + string
        return code

    def decode(self, s: str) -> List[str]:        
        words = []
        while len(s) > 0:
            index = s.find('#')
            num = int(s[:index])
            word = s[index+1:index+num+1]
            words.append(word)
            s = s[index+num+1:]        
        return words
        


