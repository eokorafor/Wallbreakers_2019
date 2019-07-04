class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        #We are given a list of lists, we can build own own matrix
        transpose = []
        counter = 0
        
        for row in A:
            for elm in row:
                temp = []
                transpose.append(temp)
            break
        
        for row in A:
            #temp = []
            #transpose.append(temp)
            for elm in row:
                transpose[counter].append(elm)
                counter = counter+1
            counter = 0
        return transpose