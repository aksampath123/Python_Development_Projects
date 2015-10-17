import random

counter = int(1)
decount = int(3)
rand_num = random.randint(1,10)

while (counter < 5):
 
  guess_num = input("Please guess the number between 1 and 10: ")
  
  try:
    int_guess_num = int(guess_num)
    guess_list.append(int_guess_num)
  except:
    print("Integer Please")
    break
    
  if int_guess_num < 1 or int_guess_num > 10:
    print("Not within the range of values")
    if(decount == 1):
      print("You ony have {} try remaining".format(decount))
    else:
      print("You ony have {} tries remaining".format(decount))
  else:
    if int_guess_num > rand_num:
       print("Your guess is too high, please try again")
       if(decount == 1):
          print("You ony have {} try remaining".format(decount))
       else:
          print("You ony have {} tries remaining".format(decount))
    elif int_guess_num < rand_num:
       print("Your guess is too low, please try again")
       if(decount == 1):
          print("You ony have {} try remaining".format(decount))
       else:
          print("You ony have {} tries remaining".format(decount))
    else:
       print("You have guess number {} correctly, and it took you {} tries".format(guess_num, counter))
       break
    
    if(decount == 0):
      print("Unfortunetely you are out of tries. The correct value is {}.".format(rand_num))
      
    counter+=1
    decount-=1
    continue
    
   
