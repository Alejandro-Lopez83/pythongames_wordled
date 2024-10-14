import random

word_list = ["bread", "fruit", "steak", "berry", "mango", "grape", "onion", "peach", "lemon", "beans"]
play_word = random.choice( word_list)
letter_index = 0
print(play_word)
count_unique_letter_playword = 0
count_letter_iterations= 0

print("The word must contain 5 letters and it is related with food\n")

user_word = input("Type in your guess: ")
try_count = 0

while try_count < 7:
    
    for i in range(len(play_word)):
        if play_word[i] == user_word[i]:
            print('YES')
        else:
            print('NO')
    
   
    #for i in user_word:
        #count_unique_letter_playword = play_word.count(i)
        #count_unique_letter_userword = user_word.count(i)

        print(i)
        
        if i in play_word and i == play_word[letter_index]:
            print(f"the letter in position {letter_index + 1} is in the right place")
        elif i in play_word:
            print(f"the letter in position{letter_index + 1} is in the incorrect place")
        else:
            print(f"the letter is not in the word")
        letter_index += 1


try_count += 1


#if play_word in range(0,6) == user_word in range(0,6):
    #print()