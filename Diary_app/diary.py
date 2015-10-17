#!/usr/bin/env python3

import datetime
import sys
import os
from collections import OrderedDict

from peewee import *

db = SqliteDatabase('diary.db') 

class Entry(Model):
  content = TextField()
  #With the parentheses included, the time will show as when we ran the script instead of the query
  timestamp = DateTimeField(default=datetime.datetime.now)
  
  class Meta:
    database = db
    
def initialize():
  """Create the database and the table if they don't exist"""
  db.connect()
  db.create_tables([Entry], safe=True)

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
    
def menu_loop():
  """Show the menu"""
  choice = None
  
  while choice != 'q':
    clear()
    print('Enter q to quit')
    for key, value in menu.items():
      print('{}) {}'.format(key, value.__doc__)) #Basically the values are functions in our OrderedDict, therefore the __doc__ will print out the associated docstring for that function
    choice = input("Please Enter the menu choice: ").lower().strip()
    
    if choice in menu:
      clear()
      menu[choice]()
  
  
  
def add_entry():
  """Add an entry"""
  print("Enter your entry. Press ctrl+d when finished.")
  data = sys.stdin.read().strip() #gathering the user input written within the system stdin.read(). strip() is used to get rid of trailing whitespaces.
  
  if data:
    data_save = input("\nSave Entry? (Y/N)".lower())
    if data_save != 'n':
      Entry.create(content = data)
      print("Saved successfully!")
      
  

def show_entry(search_query=None):
  """Show an entry"""
  entries = Entry.select().order_by(Entry.timestamp.desc())
  
  if search_query:
    entries = entries.where(Entry.content.contains(search_query))
  
  for entry in entries:
    timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
    clear()
    print('\n')
    print(timestamp)
    print('-'*len(timestamp))
    print(entry.content)
    print('\n\n'+'-'*len(timestamp))
    
    print('n) next entry')
    print('q) return to main menu')
    print('d) delete entry')
    
    next_entry = input("Action: ").lower().strip()
    if next_entry == 'q':
      break
    elif next_entry == 'd':
      delete_entry(entry)
      
def search_entries():
  """Search entries for a string"""
  search_query = input("String> ")
  show_entry(search_query)
  
  
def delete_entry(entry):
  """Delete an entry"""
  if input("Are you sure? [y/n]").lower().strip() != 'n':
    entry.delete_instance()
    print("Entry has been Deleted")
     
menu = OrderedDict([
    ('a', add_entry),
    ('v', show_entry),
    ('s', search_entries)
  ])

#Makes sure it does not run all the type, only when it is needed (thread is created)  
if __name__ == '__main__':
  initialize()
  menu_loop()
    
  
  
  