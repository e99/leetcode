class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def makePermutation(line,i):
            if i==len(S):
                answer_list.append(line)
                return 
            if S[i].isnumeric():
                makePermutation(line+S[i],i+1)
            else:     
                makePermutation(line+S[i].upper(),i+1)
                makePermutation(line+S[i].lower(),i+1)
            
        answer_list=[]
        makePermutation("",0)
        return answer_list
