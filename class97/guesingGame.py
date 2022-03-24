import random
number = random.randint(1,9)
chances = 0
print("guese a number between 1 and 9: ")
while chances<5:
    guess=int(input("enter your guess: "))
    if guess==number:
        print("CONGRATULATION")
        break
    elif guess<number:
        print("YOUR GUESS WAS TOO LOW,GUESS A HIGHER NUMBER")
    else :
        print("YOUR GUESS WAS TOO HIGH,GUESS A LOWER NUMBER")
    chances+=1
if not chances<5:
    print("YOU LOST,THE NUMBER WAS ",number)
