#the_list = ["a", 2, 3, 1, False, [1, 2, 3]]
#
#popped_item = the_list.pop(3)
#
#the_list.insert(0, popped_item)
#
#del the_list[5]
#
#for item in the_list:
#  if(item == "a" or item == False):
#    while True:
#      try:
#        the_list.remove(item)
#      except:
#        break
#        
#the_list.extend([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
#
#print(the_list)

#slice_list = list(range(20))
#
#new_slice = slice_list[0:4]
#
#new_slice2 = slice_list[len(slice_list)-4:]
#
#new_slice_list = new_slice + new_slice2
#
#print(new_slice_list)

#def sillycase(str_word):
#  new_list = list(str_word)
#  lower_list = new_list[:round(len(new_list)/2)]
#  upper_list = new_list[round(len(new_list)/2):]
#  
#  join_lower = ''.join(lower_list).lower()
#  join_upper = ''.join(upper_list).upper()
#      
#  output = join_lower + join_upper
#  return output
#
#sillycase('Treehouse')
  
#def members(my_dict={}, my_list=[]):
#  count = 0
#  for keys in my_dict:
#    for item in my_list:
#      if item == keys:
#        count += 1
#return count
#
#dictionary = {'apples':1,'bananas' : 2, 'coconuts': 3}
#list_keys = ['apples', 'coconuts', 'grapes', 'strawberries']
#
#members(dictionary,list_keys)

#dictionary = {'apples':1,'bananas' : 2, 'coconuts': 3}
#
#del dictionary['apples']
#
#print(dictionary)
#
#def word_count(new_string):
#  word_list = new_string.lower().split()
#  word_count = 0  
#  dictionary={}
#  for word in word_list:
#    if word in dictionary:
#      word_count = dictionary[word] + 1
#      dictionary.update({word: word_count})
#    else:
#      dictionary[word] = 1
#      word_count = dictionary[word] 
#  return dictionary
#
#
#word_count("I am that I am")

#def string_factory(string_value, dicts = {}):
#  list_string = []
#  for item in dicts:
#    new_string = string_value.format(**item)
#    list_string.append(new_string)
#  return list_string
#
#dicts = [
#    {'name': 'Michelangelo',
#     'food': 'PIZZA'},
#    {'name': 'Garfield',
#     'food': 'lasanga'},
#    {'name': 'Walter',
#     'food': 'pancakes'},
#    {'name': 'Galactus',
#     'food': 'worlds'}
#]
#
#string = "Hi, I'm {name} and I love to eat {food}!"
#
#string_factory(string, dicts)



#my_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],'Kenneth Love': ['Python Basics', 'Python Collections']}
#
#def most_classes(my_dict):
#  teacher_list = []
#  max_count = []
#  for key in my_dict:
#    teacher_list.append(key)
#  for value in my_dict.values():
#    count = 0
#    for classes in value:
#        count += 1
#    max_count.append(count)
#  max_teacher = teacher_list[max_count.index(max(max_count))]
#  print(max_teacher)
#  return max_teacher
#
#def num_teacher(my_dict):
#  teacher_list = []
#  max_count = []
#  for key in my_dict:
#    teacher_list.append(key)
#  num_teach = len(teacher_list)
#  return num_teach
#
#def stats(my_dict):
#  teacher_list = []
#  for key in my_dict:
#    my_list = []
#    my_list.append(key)
#    my_list.append(len(my_dict[key]))
#    teacher_list.append(my_list)
#  print(teacher_list)
#  return teacher_list
#
#def courses(my_dict):
#  course_list = []
#  for value in my_dict:
#    print(value)
#    for course in my_dict[value]:
#      course_list.append(course)
#  return course_list
#      
#
#def stringcases(string):
#  four_tupple = ()
#  upper = string.upper()
#  lower = string.lower()
#  titlecase = string.title()
#  reverse = string[::-1]
#  four_tupple = (upper, lower, titlecase, reverse)
#  return four_tupple
#  
#def combo(list1, string):
#  list2 = list(string)
#  list_length = len(list1)
#  tuple_list = []
#  for i in range(list_length):
#      tuples = (list1[i],list2[i])
#      tuple_list.append(tuples)
#  print(tuple_list)
#           
#combo(['swallow', 'snake', 'parrot'], 'abc')

import random
#
#def nchoices(iterable, integer):
#  random_list = []
#  for i in range(integer):
#    random1 = random.choice(iterable);
#    random_list.append(random1)
#  return random_list
#  
#nchoices([(1,2),(3,4),(4,5),(6,7),("Akshay","Sampath")],5)

map_t = (0, 1, 2, 4, 5, 6, 7, 8, 9)

map_t_sort = map_t.sort()

print(map_t_sort)


       
        
        
    
  
  


