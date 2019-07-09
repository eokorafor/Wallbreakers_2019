class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sub = collections.Counter(p)
        s_colct = collections.Counter(s)
        if len(s_colct) == 0: #empty check
            return []
        if len(sub) > len(s_colct): #no possible anagrams
            return []
        
        indices = []
        pLen = len(p)
        sLen = len(s)
        runS = collections.Counter(s[:pLen]) 
        for index in range(pLen,sLen):
            if runS == sub:
                indices.append(index-pLen)
            runS[s[index-pLen]] -= 1
            runS[s[index]] += 1
            if runS[s[index-pLen]] == 0:  #If char empty delete it (would mess up comparison)
                del runS[s[index-pLen]]    
            if index == sLen-1 and runS == sub:  #get last comparison
                indices.append(index-pLen+1)
        return indices
        
        