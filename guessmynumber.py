#guess my number game
x=0           #initializing value of x
while(x<16):  #condition checking
 x=(((x+0)*2)+1) 
 print("Guess my number \nThe game begins!") 
 print("You have five chances.All the best.")
 guess=int(input("Guess a number between 1 and 40 : ")) #taking input from the user
 i=1    #initializing value of i
 while(guess!=x): 
  if i==5:  # checks whether you have used all your chances
   print("Oops!You have used all your chances.You lost this game.")
   print("Retry")
   break   #loop termination
  elif guess>x:  #checks whether your guessed number is higher than the actual number
   print("Your guess is higher than the actual number.Try again.")
  elif guess<x:   #checks whether your guessed number is lower than the actual number
   print("Your guess is lower than the actual number.Try again.")     
  guess=int(input("guess again :"))
  i+=1    #incrementing the value of i
 if guess==x:  #checks whether your guess is correct
  print("You Won! \nCongratulations")
  print("you wanna try again")
