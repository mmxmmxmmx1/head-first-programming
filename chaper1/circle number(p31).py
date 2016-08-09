from random import randint
secret=randint(1,10)
print("Welcome")
g=0
while g!=secret:
 guess=input("guess the number: ")
 g=int(guess)
 
 if g==secret:
  print("you win")
 else:
   if g>secret:
    print("too high")
   else:
     print("too low")
print("game over")
