#word scrambler description
while True:
    print("Welcome to the Word Scrambler!")
    print("Choose Pig Latin, Flip, or Scramble!")
    print("")
    print("")
    print("")
    user_input = input("What would you like to do? Pig Latin, Flip, or Scramble: ")


#the important stuff


    if user_input == "Pig Latin" or user_input == "pig latin" or user_input == "PIG LATIN":
        pyg = 'ay'
        original = input("Enter a word: ")
        if len(original) and original.isalpha() > 0:
            word = original.lower()
            first = word[0]
            new_word = word[1:len(word)] + first + pyg
            print(new_word)
        else:
            print("Can't work. Try again.")
    if user_input == "Flip" or user_input == "flip" or user_input == "FLIP":
        while True:
            def reverse(string):
                return string[::-1]
            print(reverse(str(input("Enter a word: "))))
            break
    if user_input == "Scramble" or user_input == "scramble" or user_input == "SCRAMBLE":
        wrd = input("Enter a 5 letter word: ")
        print(wrd[4], wrd[2], wrd[0], wrd[3], wrd[1])
    print("")
    print("")
    print("")
    user_input = input("Would you like to play again? Y/N: ")
    if user_input == "Y" or user_input == "y":
        continue
    else:
        break
