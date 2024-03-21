import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")

# Pedir selección de dificultad
print ("Seleccione el nivel de dificultad deseado: (1) Fácil, (2) Medio, (3) Difícil")
difficulty = (input("Ingrese una opción "))

while (not difficulty.isdigit()) or (int(difficulty) not in [1,2,3]):
    print ("Opción incorrecta. Por favor, seleccione 1, 2 o 3 para la dificultad")
    print ("Seleccione el nivel de dificultad deseado: (1) Fácil, (2) Medio, (3) Difícil")
    difficulty = (input("Ingrese una opción "))

# Transformo difficulty en int para comparar en difficultWord
difficulty = int (difficulty)

def difficultWord (secret_word, difficulty):
    word = []
    if (difficulty == 1 ):
        vowels = "aeiou"
        for letter in secret_word:
            if (letter in vowels):
                word.append(letter)
            else:
                word.append ("_")
    elif (difficulty == 2):
        index = 0
        for letter in secret_word:
            if (index == 0) or (index == (len(secret_word) - 1)):
                word.append(letter)
            else:
                word.append("_")
            index += 1
    else:
            word = ["_"] * len(secret_word)
    return word

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Completo letters según dificultad seleccionada
letters = difficultWord (secret_word,difficulty)

# Declaro variable con palabra parcialmente adivinada segun dificultad y la imprimo
word_displayed = "".join(letters)
print(f"Palabra: {word_displayed}")

# Comienza el juego

while (max_attempts != 0):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    #Verificar si la letra es correcta
    if (len(letter)!= 1) or (not letter.isalpha()):
        print ("Error: Debes ingresar una única letra")
        continue
    # Verificar si la letra ya ha sido adivinada
    elif (letter in guessed_letters):
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Verificar si la letra está en la palabra secreta
    elif (letter in secret_word): 
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        max_attempts -= 1 
        # Muestro palabra anterior ya que no hubo cambios y corto ejecución
        print(f"Palabra: {word_displayed}")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Agregar letras adivinadas
    index = 0
    for letter in secret_word:
        if letter in guessed_letters:
            letters[index] = letter
        index += 1
    
    # Mostrar la palabra parcialmente adivinada
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")