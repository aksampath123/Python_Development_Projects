shopping_list = list()
print("Please enter an item into your shooping list")
print("Please type 'DONE' when you have completed the shoping list")

while True:
  new_item = input("> ")
  
  if new_item == 'DONE':
    break
    
  shopping_list.append(new_item)
  print("Added: List has {} item.".format(len(shopping_list)))
  continue
 
print("This is your list:")

for item in shopping_list:
  print(item)
  
  