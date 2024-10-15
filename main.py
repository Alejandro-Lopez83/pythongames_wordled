import random

word_list = ["bread", "fruit", "steak", "berry", "mango", "grape", "onion", "peach", "lemon", "beans"]
icons_list = []
letter_list= []

play_word = random.choice( word_list)
print(play_word)
letter_index = 0
count_unique_letter_playword = 0
count_letter_iterations= 0

print("The word must contain 5 letters and it is related with food\n")

try_count = 0

def menu():
    print(f"\n\n*********************************************************************")
    print(f"**                            WELCOME TO                           ** ")
    print(f"**********************          WORDLE         ********************** ")
    print(f"**                                                                 ** ")
    print(f"*********************************************************************\n\n")

menu()

while try_count < 6:
    letter_index=0
    user_word = input("--> Type in your guess: ").lower().strip()
    number = False
    for i in user_word:
        aux_to_number = 0
        try:
            aux_to_number = int(i)
            number = True
            break
        except Exception:
            pass
    while len(user_word) !=5 or number == True:
            if len(user_word) != 5:
                print("\n            WARNING: The word MUST HAVE 5 letters :WARNING\n")
            elif len(user_word) != 5 and number == True:
                print("\n            WARNING: Only letters are valid :WARNING\n")
            elif number == True:
                print("\n            WARNING: Only letters are valid :WARNING\n")
            
            user_word = input("--> Type in your guess: ").lower().strip()
            number = False
            for i in user_word:
                aux_to_number = 0
                try:
                    aux_to_number = int(i)
                    number = True
                    break
                except Exception:
                    pass
   
    

    if user_word==play_word:
            print("\n                       ********************")
            print("                       ********************")
            print("                       **    YOU WIN!!   **")
            print("                       ********************")
            print("                       ********************\n")
            break


    for i in user_word:
        count_unique_letter_playword = play_word.count(i)
        count_unique_letter_userword = user_word[0:letter_index+1].count(i)
 
              
        if i in play_word and i == play_word[letter_index]:
            print(f"The letter ", end="")
            print("|",i,"|", end="")
            print(f" in position {letter_index + 1} is in the right place")
        elif i in play_word:
            if count_unique_letter_userword>count_unique_letter_playword:
                print(f"The letter ", end="")
                print("|",i,"|", end="")
                print(f" in position {letter_index + 1} is already covered")
            else:
               print(f"The letter ", end="")
               print("|",i,"|", end="")
               print(f" in position {letter_index + 1} is in the incorrect place")
        else:
            print(f"The letter ", end="")
            print("|",i,"|", end="")
            print(" is not in the word <-------------")
        
        letter_index += 1

    if user_word != play_word and try_count<5:
        print("\n\n        |                                   |")
        print(f"        |      YOU HAVE {5-try_count} ATTEMPS LEFT      |")
        print("        |     TRY AGAIN WITH A NEW WORD     |")
        print("        |                                   |\n\n")

    else:
        print("\n\n                       ********************")
        print("                       ********************")
        print("                       **   YOU LOSE!!   **")
        print("                       ********************")
        print("                       ********************\n")

    try_count+=1
