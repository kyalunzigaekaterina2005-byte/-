import random

words = {
    "заря": "яркое освещение горизонта перед восходом или заходом солнца",
    "шепот": "тихая речь, при которой звуки произносятся без участия голосовых связок",
    "лабиринт": "сложная структура из запутанных путей, ходов, коридоров или дорожек",
    "волшебство": "сверхъестественные действия или явления, кажущиеся чудом",
    "улыбка": "мимика лица, губ, глаз, показывающая расположение к смеху"
}

word_list = list(words.keys())
secret_word = random.choice(word_list)
definition = words[secret_word]

human = [
    """
    _______
  |/   
  |   
  |   
  |    
  |   
  |
  |________""", 
    """
    _______
  |/   |
  |   
  |   
  |    
  |   
  |
  |________""", 
    """
    _______
  |/   |
  |   (_)
  |   
  |   
  |
  |
  |________""", 
    """
    _______
  |/   |
  |   (_)
  |    |
  |    |
  |
  |
  |________""", 
    """
    _______
  |/   |
  |   (_)
  |   \|
  |    |
  |
  |
  |________""", 
    """
   _______
  |/   |
  |   (_)
  |   \|/
  |    |
  |
  |
  |________""", 
    """
    _______
  |/   |
  |   (_)
  |   \|/
  |    |
  |   /
  |
  |________""", 
    """
    _______
  |/   |
  |   (_)
  |   \|/
  |    |
  |   / \\
  |
  |________""", 
]

letters = [] 
errors = 0            
max_errors = 7

print("Добро пожаловать в игру виселица")
print(f"Подсказка: {definition}")

while errors < max_errors:
    print(human[errors])
    
    display_word = ""
    for letter in secret_word:
        if letter in letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(f"Слово: {display_word}")
    
    if "_" not in display_word:
        print("\nПоздравляем! Вы угадали слово!")
        break

    version = input("Введите букву: ").lower()

    if len(version) != 1:
        print("Пожалуйста, введите только одну букву")
        continue
    
    if version in letters:
        print("Вы уже вводили эту букву")
        continue

    if version in secret_word:
        print("Буква есть в слове")
    else:
        print("Такой буквы нет")
        errors += 1
        print(f"Осталось попыток: {max_errors - errors}")

if errors == max_errors:
    print(human[errors])
    print("Вы проиграли!")
    print(f"Было загадано слово: {secret_word}")