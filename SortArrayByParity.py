class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #split the array into two and then concatenate
        even = []
        odd = []
        for elm in A:
            if elm%2 == 0:
                even.append(elm)
            else:
                odd.append(elm)
        even.sort()
        odd.sort()
        return even+odd
        