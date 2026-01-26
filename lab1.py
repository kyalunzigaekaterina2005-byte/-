import random

bye = 0

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")

while bye < 3:
    user_answer = input("> ")

    if user_answer == "ПОКА!":
        bye += 1
        
        if bye < 3:
            year = random.randint(1930, 1950)
            print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
            
    elif user_answer.isupper() and user_answer != "":
        bye = 0
        year = random.randint(1930, 1950)
        print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
        
    else:
        bye = 0  
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")

print("ДО СВИДАНИЯ, МИЛЫЙ!")
