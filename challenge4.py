vCount = 0
consonantCount = 0
word = input("Give me a word:")
def analyze_word():
    global vCount, consonantCount #allows the function to change the variables outside of it.
    for letter in word:
        if letter in "aeiouAEIOU":
            vCount += 1
        else: consonantCount += 1
    print("Vowels:", vCount, "Consonants:", consonantCount)
analyze_word()