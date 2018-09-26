
i=0
while i < 10:
   print ("i is now {}".format(i))
   i +=1


available_exit = ["east", "north east", "south"]
chosen_exit = ""
while chosen_exit not in available_exit:
   chosen_exit = input("Please choose a direction: ")
   if chosen_exit == "quit":
      print ("Game Over")
      break
else:
   print ("aren't you glad you got out of there")



import random
highest = 10
answer = random.randint(1, highest)

print ("Please guess a number between 1 and {}: ".format(highest))
guess = 1
while (guess != 0):  # enter 0 to quit
   guess = int(input())
   if guess == answer:
      print ("You guess it")
      break
   elif guess < answer:
      print ("Guess higher")
   else:
      print ("Guess lower")


