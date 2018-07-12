def uniqueMorseRepresentations(words):

    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    words1 = set()
    for word in words:
        string = ""
        for char in word:
            string += morse_code[ord(char) - ord('a')]
        words1.add(string)
        
    return len(words1)
                


words1=["gin","zen","gig","msg"]
words2 = ["a", "z", "g", "m"]
words3 = ["bhi", "vsv", "sgh", "vbi"]
words4 = ["a", "b", "c", "d"]
words5 = ["hig", "sip", "pot"]
print(uniqueMorseRepresentations(words1))
print(uniqueMorseRepresentations(words2))
print(uniqueMorseRepresentations(words3))
print(uniqueMorseRepresentations(words4))
print(uniqueMorseRepresentations(words5))
