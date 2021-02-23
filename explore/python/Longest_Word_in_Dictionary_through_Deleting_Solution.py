class Solution:
    def findLongestWord(self, s, W):
        def match(x, y):
            if not y: 
                return True
            if not x: 
                return False
            
            if x[0]==y[0]: 
                return match(x[1:], y[1:])
            else:
                return match(x[1:], y)
        
        
        for w in sorted(W, key = lambda x: (-len(x),x)):
            if match(s,w):
                return w
        return ''