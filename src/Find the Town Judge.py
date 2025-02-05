class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a, b = -1, -1
        ret1 = [0] * (n+1)
        ret2 = [0] * (n+1)
        for pair in trust:
            ret1[pair[0]] = 1
            ret2[pair[1]] += 1
        for i in range(1, n+1):
            if ret1[i] == 0:
                a = i
            if ret2[i] == n-1:
                b = i
        if a == -1 or b == -1:
            return -1
        if a == b:
            return a
        return -1
    