shopping_list = []

def show_help():
  print("Enter the items/amount for your shopping list")
  print("Enter DONE once you have completed the list, Enter Help if you require assistance")
  
def add_to_list(item):
  shopping_list.append(item)
  print("Added! List has {} items.".format(len(shopping_list)))
  
def show_list():
  print("Here is your list")
  for item in shopping_list:
    print(item)
  
show_help()

while True:
  new_item = input("item>")
  
  if new_item == 'DONE':
    break
  elif new_item == 'HELP':
    show_help()
    continue
  elif new_item == 'SHOW':
    show_list()
    continue
  else:
    add_to_list(new_item)
    continue
  
show_list()