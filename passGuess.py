import random

easy_words =["apple","train","tiger","money","india"]
medium_words=["python","bottle","monkey","planet","laptop"]
hard_words=["elephant","diamond","umbrella","computer","mountain"]

print("WELCOME TO THE PASSWORD GUESSING GAME")
print("CHOOSE A DIFFICULTY LEVEL: easy,medium ,hard")

level=input('Enter difficulty:').lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("INVALID CHOICE ,DEFAULTING TO EASY LEVEL")
    secret = random.choice(easy_words)    
attempt =0
print("\n Guess the secret password")   

#Game loop
while True:
    guess = input("Enter your guess:").lower()
    attempt +=1

    if guess ==secret:
        print(f'Congratulations! You guessed it in {attempt} attempt.')
        break

    #give a hint
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] ==secret[i]:
            hint += guess[i]
        else:
            hint +="_"
        print("Hint:",hint)     
print("GAME OVER")