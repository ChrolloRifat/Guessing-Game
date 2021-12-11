store = 4 
trial = 0 
while trial < 3: 
  entry = int(input("Guess the Number: ")) 
if entry == store: 
  print("Congratulations! You Won ") 
  break 
elif trial < 3: 
  print("Try Again")
    trial += 1
else:
    print("You failed !!!")
print("You have reached Level 2!!") 
store = store * 2 
trial = 0 
while trial < 3: 
  entry = int(input("Guess the Number: "))
if entry == store: print("Congratulations! You Won ") 
  break
elif trial < 3: 
  print("Try Again") 
  trial += 1 
else: print("You failed !!!") 
print('You have completed the game!!')
