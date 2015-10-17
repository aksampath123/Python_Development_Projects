user_string = input("What's your word? ")
user_length = input("Which letter index would you like to be returned (Ratio/Integer)? ")

try:
  our_num = int(user_length)
except:
  our_num = float(user_length)
  
if not '.' in user_length:
  print(user_string[our_num-1])
else:
  ratio = round(len(user_string) * our_num)
  print(user_string[ratio-1])
  