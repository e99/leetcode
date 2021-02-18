class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A or len(A) < 3: return 0
        res = 0
        cnt, diff = 2, A[1] - A[0]
        for i in range(2, len(A)):
            if A[i] - A[i-1] == diff:
                cnt += 1
            else:
                if cnt > 2: res += ((cnt-1)*(cnt-2))//2
                cnt, diff = 2, A[i] - A[i-1]
        if cnt > 2: res += ((cnt-1)*(cnt-2))//2
        return res