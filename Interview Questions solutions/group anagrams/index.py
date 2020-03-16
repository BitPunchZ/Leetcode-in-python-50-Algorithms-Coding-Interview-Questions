class Solution:
    def findHash(self,s):
        return ''.join(sorted(s))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        m = {}

        for s in strs:
            hashed = self.findHash(s)
            if(hashed not in m):
                m[hashed] = []
            m[hashed].append(s)
        
        for p in m.values():
            answers.append(p)
        
        return answers

