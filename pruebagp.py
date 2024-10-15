import random

word_list = ["bread", "fruit", "steak", "berry", "mango", "grape", "onion", "peach", "lemon", "beans"]
play_word = random.choice(word_list)  # Elegir la palabra aleatoria de la lista
print("The word must contain 5 letters and it is related with food\n")

try_count = 0  # Contador de intentos

while try_count < 7:
    user_word = input(f"Attempt {try_count + 1}: Type in your guess: ").lower()

    # Validación de la longitud de la palabra
    if len(user_word) != 5:
        print("Please enter a 5-letter word.")
        continue

    if user_word == play_word:
        print("Congratulations! You've guessed the word!")
        break

    letter_index = 0  # Reiniciar el índice para cada nuevo intento
    for i in user_word:
        count_unique_letter_playword = play_word.count(i)
        count_unique_letter_userword = user_word[:letter_index + 1].count(i)

        # Verificar si la letra está en la posición correcta
        if i == play_word[letter_index]:
            print(f"The letter '{i}' is in the right place (position {letter_index + 1}).")
        
        # Verificar si la letra está en la palabra pero en la posición incorrecta
        elif i in play_word:
            if count_unique_letter_userword > count_unique_letter_playword:
                print(f"The letter '{i}' is not in the word or is repeated too many times.")
            else:
                print(f"The letter '{i}' is in the word but in the wrong place.")

        # Verificar si la letra no está en la palabra
        else:
            print(f"The letter '{i}' is not in the word.")

        letter_index += 1

    try_count += 1

# Después del bucle, si el jugador no adivinó correctamente:
if user_word != play_word:
    print(f"Sorry, you've used all your attempts. The word was: {play_word}")
