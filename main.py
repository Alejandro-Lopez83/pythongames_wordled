import random

word_list = ["bread", "fruit", "steak", "berry", "mango", "grape", "onion", "peach", "lemon", "beans"]
play_word = random.choice( word_list)
letter_index = 0
count_unique_letter_playword = 0
count_letter_iterations= 0

print("The word must contain 5 letters and it is related with food\n")

try_count = 0

while try_count < 6:
    letter_index=0
    user_word = input("Type in your guess: ").lower().strip()
    while len(user_word) !=5:
        print("The word MUST HAVE 5 letters\n")
        user_word = input("Type in your guess: ").lower().strip()

    if user_word==play_word:
            print("YOU WIN!!")
            break


    for i in user_word:
        count_unique_letter_playword = play_word.count(i)
        count_unique_letter_userword = user_word[0:letter_index+1].count(i)
 

        print(i)
        
        if i in play_word and i == play_word[letter_index]:
            print(f"The letter in position {letter_index + 1} is in the right place")
        elif i in play_word:
            if count_unique_letter_userword>count_unique_letter_playword:
                print(f"The letter {i} is already filled")
            else:
                print(f"The letter in position{letter_index + 1} is in the incorrect place")
        else:
            print(f"The letter is not in the word")
        
        letter_index += 1

    if user_word != play_word and try_count<5:
        print(f"\nYOU HAVE {5-try_count} ATTEMPS LEFT")
        print("TRY AGAIN WITH A NEW WORD")
    else:
        print("YOU LOSE")

    try_count+=1
        
        
    




#if play_word in range(0,6) == user_word in range(0,6):
    #print()