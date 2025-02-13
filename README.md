# pythongames_wordled

# 🎮 Food Wordle | Wordle de Comidas

[English](#english) | [Español](#español)

# English

A Python-based Wordle game focused on food-related words. Players have 6 attempts to guess a 5-letter word.

## 📝 Description

This is a guessing game based on the popular Wordle, but with a specific food theme. The game randomly selects a word from a predefined list of food-related words in English, and the player must guess it within 6 attempts.

## 🎯 Features

- Food-related words
- Console interface with emojis
- 6 attempts to guess
- Visual feedback for each letter:
  - 🟢 Correct letter in correct position
  - 🟠 Correct letter in wrong position
  - 🔴 Incorrect letter or already covered

## 🚀 How to Play

1. Run the Python script
2. You'll see a welcome screen
3. Press ENTER to start
4. Input 5-letter food-related words
5. Receive feedback after each attempt
6. Guess the word in 6 attempts or less!

## 📋 Requirements

- Python 3.x
- No additional libraries required

## 💻 Installation

1. Clone this repository:
```bash
git clone <repository-url>
```

2. Navigate to the project directory:
```bash
cd food-wordle
```

3. Run the game:
```bash
python wordle.py
```

## 🎮 Game Example

```
*********************************************************************
**                            WELCOME TO                           ** 
**********************          WORDLE         ********************** 
**                                                                 ** 
*********************************************************************

     The word must contain 5 letters and it is related with food

              🟢 Letter is in the RIGHT position!!                                       
              🟠 Letter is in wrong position!!                                       
              🔴 Letter is not in the word or is already covered                                       

                       PRESS ENTER TO PLAY!!!!!
```

---

# Español

Un juego de Wordle en Python centrado en palabras relacionadas con alimentos. Los jugadores tienen 6 intentos para adivinar una palabra de 5 letras.

## 📝 Descripción

Este es un juego de adivinanzas basado en el popular Wordle, pero con una temática específica de alimentos. El juego selecciona aleatoriamente una palabra de una lista predefinida de alimentos en inglés, y el jugador debe adivinarla en un máximo de 6 intentos.

## 🎯 Características

- Palabras relacionadas con alimentos
- Interfaz en consola con emojis
- 6 intentos para adivinar
- Retroalimentación visual para cada letra:
  - 🟢 Letra correcta en posición correcta
  - 🟠 Letra correcta en posición incorrecta
  - 🔴 Letra incorrecta o ya cubierta

## 🚀 Cómo Jugar

1. Ejecuta el script de Python
2. Verás una pantalla de bienvenida
3. Presiona ENTER para comenzar
4. Introduce palabras de 5 letras relacionadas con alimentos
5. Recibe retroalimentación después de cada intento
6. ¡Adivina la palabra en 6 intentos o menos!

## 📋 Requisitos

- Python 3.x
- No se requieren bibliotecas adicionales

## 💻 Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
```

2. Navega al directorio del proyecto:
```bash
cd food-wordle
```

3. Ejecuta el juego:
```bash
python wordle.py
```

## 🎮 Ejemplo de Juego

```
*********************************************************************
**                            WELCOME TO                           ** 
**********************          WORDLE         ********************** 
**                                                                 ** 
*********************************************************************

     The word must contain 5 letters and it is related with food

              🟢 Letter is in the RIGHT position!!                                       
              🟠 Letter is in wrong position!!                                       
              🔴 Letter is not in the word or is already covered                                       

                       PRESS ENTER TO PLAY!!!!!
```

## 🛠️ Technical Details / Detalles Técnicos

### Word List / Lista de Palabras
```python
word_list = ["bread", "fruit", "steak", "berry", "mango", 
             "grape", "onion", "peach", "lemon", "beans"]
```

### Code Structure / Estructura del Código
- Input validation / Validación de entrada
- Random word selection / Selección aleatoria de palabra
- Letter comparison system / Sistema de comparación de letras
- Victory/defeat conditions / Condiciones de victoria/derrota

## ✨ Possible Improvements / Posibles Mejoras

- Add more words / Añadir más palabras
- Implement different food categories / Implementar diferentes categorías de alimentos
- Add a scoring system / Agregar un sistema de puntuación
- Include a graphical interface / Incluir una interfaz gráfica
- Add language support / Agregar soporte para múltiples idiomas

## 🤝 Contributing / Contribuir

1. Fork the project / Haz un Fork del proyecto
2. Create your feature branch / Crea una rama para tu función
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes / Haz commit de tus cambios
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch / Push a la rama
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request / Abre un Pull Request
