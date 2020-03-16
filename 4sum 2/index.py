class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
      m = {}
      ans = 0

      for i in range(0,len(A)):
        x = A[i]
        for j in range(0,len(B)):
          y = B[j]
          if(x+y not in m):
            m[x+y] = 0
          m[x+y]+=1

      for i in range(0,len(C)):
        x = C[i]
        for j in range(0,len(D)):
          y = D[j]
          target = -(x+y)
          if(target in m):
            ans+=m[target]

      return ans