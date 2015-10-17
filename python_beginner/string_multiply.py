#num1 = int('5')
#num2 = float('5')
#name_list2 = "Akshay Sampath"
#full_name = name_list2.split()
#name_list = "Hi, I'm Treehouse".split()
#
#mergedlist = full_name + name_list
#
#greeting = ' '.join(mergedlist)
#print(greeting)

#print(str(num1) + str(num2))
#days = int('7') * num1 * int('52')
#print(days)
#string_days = str(days);
#summary = ("I am {} days old".format(days))
#print(summary)

import random

new_list = [1, 2, 3]
#print(new_list)

def add_list(myList=[]):
  sum_array = sum(myList)
  return sum_array  
  
def summarize(list_sum, myList=[]):
  print("the sum of {} is {}".format(myList, 6)) 
  return "the sum of {} is {}".format(myList, list_sum)   

def random_num(num):
  rand_int = random.randint(1,num)
  print (rand_int)
  return rand_int

random_num(10)

