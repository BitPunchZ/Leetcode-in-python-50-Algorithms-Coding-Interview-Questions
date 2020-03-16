class Solution:
    def isPalin(self, seg):
        i = 0
        j = len(seg)-1
        while(i < j):
            if(seg[i] != seg[j]):
                return False
            i += 1
            j -= 1
        return True

    def dfs(self, s: str):
        if(len(s) == 0 and len(self.temp) > 0):
            self.res.append(self.temp[:])
            return
        n = len(s)+1
        for i in range(1, n):
            seg = s[0:i]
            if(self.isPalin(seg)):
                self.temp.append(seg)
                self.dfs(s[i:])
                self.temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.temp = []
        self.dfs(s)
        return self.res
