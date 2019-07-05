class Solution:
    def reverseVowels(self, s: str) -> str:
        reverse = []
        vowelSpots = []
        vowels = []
        counter = 0
        for letter in s: 
            if letter.lower() in "aeiou":
                vowelSpots.append(counter)
                vowels.append(letter)
            counter = counter + 1
        vowels.reverse()
        if len(vowels) == 0:
            return s
            
        n_count = 0
        for index in range(len(s)):
            if index == vowelSpots[n_count]:
                reverse.append(vowels[n_count])
                if n_count != len(vowels)-1:
                    n_count = n_count + 1
            else:
                reverse.append(s[index])
        return "".join(reverse)
        