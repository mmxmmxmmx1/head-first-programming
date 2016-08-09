print("Welcome !")
g = input("Guess the number: ")
guess = int(g)
if guess == 3:
    print("太小")
if guess == 5:
    print("你贏了 !")
if guess == 7:
    print("太大了!")
if guess == 8:
    print("太大了!")
else:
    print("You lose !")
    print("Game over !")
 
