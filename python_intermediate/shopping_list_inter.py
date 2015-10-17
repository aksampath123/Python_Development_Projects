shopping_list = []

def show_help():
  print("\nSeperate each item with a comma.")
  print("Enter DONE once you have completed the list, Enter Help if you require assistance and enter SHOW to see list at any time")
  
def remove_item(index):
  pop_item = shopping_list.pop(index)
  print("Item {} removed".format(pop_item))
  
def show_list():
  count = 1
  print("Here is your list")
  for item in shopping_list:
    print("{}:{}".format(count,item))
    count += 1
  
show_help()

while True:
  new_item = input("item(s)>")
  
  if new_item == 'DONE':
    break
  elif new_item == 'HELP':
    show_help()
    continue
  elif new_item == 'SHOW':
    show_list()
    continue
  elif new_item == 'REMOVE':
    show_list()
    index = input("Which item would you like to be removed: ")
    int_index = int(index) - 1 
    remove_item(int_index)
  else:
    new_list = new_item.split(",")
    index = input("Add this at a certain spot? press enter for the end of the list, or give me a number. Currently have {} items in the list. ".format(len(shopping_list)))
    
    if index:
      stop = int(index) - 1
      for item in new_list:
        shopping_list.insert(stop,item.strip())
        stop += 1
    
    else:
      for item in new_list:
        shopping_list.append(item.strip())
      