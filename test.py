import random

word_list = ["bread", "fruit", "steak", "berry", "mango", "grape", "onion", "peach", "lemon", "beans"]
icons_list = []
letter_list= []

play_word = random.choice( word_list)
print(play_word)
letter_index = 0
count_unique_letter_playword = 0
count_letter_iterations= 0



try_count = 0

def menu():
    print(f"\n\n*********************************************************************")
    print(f"**                            WELCOME TO                           ** ")
    print(f"**********************          WORDLE         ********************** ")
    print(f"**                                                                 ** ")
    print(f"*********************************************************************\n\n")
menu()

print("            The word must contain 5 letters and it is related with food\n")


print("                    🟢 Letter is in the RIGHT position!!                                       ")
print("                    🟠 Letter is in wrong position!!                                       ")
print("                    🔴 Letter is not in the word or is already covered                                        ")



input('                          PRESS ENTER TO PLAY!!!!!')
print('                        ----------------------------                         ')



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
   
    


    letter_list= []
    icons_list= []
    for i in user_word:
        count_unique_letter_playword = play_word.count(i)
        count_unique_letter_userword = user_word[0:letter_index+1].count(i)
 
              
        if i in play_word and i == play_word[letter_index]:
            letter_list.append(i)
            icons_list.append("🟢")
           
        elif i in play_word:
            if count_unique_letter_userword>count_unique_letter_playword:
                letter_list.append(i)
                icons_list.append("​🔴​")
            else:
               letter_list.append(i)
               icons_list.append("🟠​​")
        else:
            letter_list.append(i)
            icons_list.append("​🔴​")
        
        letter_index += 1

    print( ' ','   '.join(letter_list))
    print(' ','  '.join(icons_list))

    if user_word==play_word:
            print("\n                       ********************")
            print("                       ********************")
            print("                       **    YOU WIN!!   **")
            print("                       ********************")
            print("                       ********************\n")
            break
    
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
