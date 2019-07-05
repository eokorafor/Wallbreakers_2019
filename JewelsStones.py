class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if len(S) == 0 or len(J) == 0:
            return 0
        count = 0
        jewels = {J[i]: i for i in range(len(J))}
        
        for stone in S:
            if stone in jewels:
                count += 1
    
        return count