#Anagrams.py (Lab 5) [Shane Roeseberg]

def are_anagrams(word1, word2):
    """Determines if both words entered are anagrams by sorting both 
    words and comparing both words to look for identical characters 
    between words (two words are anagarms only if they contain the 
    exact same characters)"""
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    if word1_sorted == word2_sorted:
        return True
    else:
        return False

def main():

    print("== Anagrams ==")
    print("Type 'stop' at any point to exit the program.")
    print("\n")

    while True:

        two_words = input("Enter a word: ")

        if two_words.upper() == "STOP":
            print("\n")
            print("== Program Exit ==")
            break

        two_words_2 = input("Enter another word: ")

        if two_words_2.upper() == "STOP":
            print("\n")
            print("== Program Exit ==")
            break

        word1 = two_words
        word2 = two_words_2

        if are_anagrams(word1, word2):
            print("\n")
            print("The words are anagrams.")
            print("\n")
        else:
            print("\n")
            print("The words are not anagrams.")
            print("\n")
        
if __name__ == "__main__":
    main()