class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        answer_list=[]
        soldier_list=[ [] for i in range(100) ]
        m=len(mat)
        n=len(mat[0])
        index=0
        
        for i in range(m):
            num=0
            for j in mat[i]:
                if j==0:
                    break
                else:
                    num+=1
            soldier_list[num].append(i)
        
        for i in soldier_list:
            if index==k:
                break
            if len(i)==0:
                continue
            else:
                for j in range(len(i)):
                    if index==k:
                        break
                    answer_list.append( i.pop(0) )
                    index+=1
        return answer_list