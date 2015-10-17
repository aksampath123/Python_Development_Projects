list1 = []

input_str1 = input("Please input a word: ")

str1 = input_str1.lower()

list1 = list(str1)

for item in list1:
  if item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'u':
    while True:
      try:
        list1.remove(item)
      except:
        break

output = ''.join(list1).capitalize()

print(output)