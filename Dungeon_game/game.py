import sys

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll

class Game:

  def setup(self):
    self.player = Character()
    self.monsters = [Goblin(), Troll(), Dragon()]
    
    self.monster = self.get_next_monster()
  
  def get_next_monster(self):
    try:
      return self.monsters.pop(0)
    except IndexError:
      return None
  
  def monster_turn(self):
    if self.monster.attack():
      print("Attack has been initiated by {}".format(self.monster))
      dodge = input("Would you like to dodge the attack,(Y/N)").lower()
      if dodge == 'y':
        if self.player.dodge():
          print("Dodge successful")
        else:
          print("You've been hit")
          self.player.hit_points -= 1
      else:
        print("{} would not like to dodge, {} has hit you for 1 point".format(self.player.name, self.monster))
        self.player.hit_points -= 1
    else:
      print("{} is not attacking".format(self.monster))
  
  def player_turn(self):
    player_choice = input("[A]ttack, [R]est, [Q]uit").lower()
    if player_choice == 'a':
      print("You are attacking {}".format(self.monster))
      if self.player.attack():
        if self.monster.dodge():
          print("{} has dodged this attack".format(self.monster))
        else:
          if self.player.level_up():
            self.monster.hit_points -= 2
          else:
            self.monster.hit_points -= 1
          print("You hit {} with yout {}!".format(self.monster, self.player.weapon))
      else:
        print("You missed")
    elif player_choice == 'r':
      self.player.rest()
    elif player_choice == 'q':
      sys.exit()
    else:
      self.player_turn()
    
  def clean_up(self):
    if self.monster.hit_points <= 0:
      self.player.experience += 5
      print("You killed {}!".format(self.monster))
      self.monster = self.get_next_monster()
      
  def __init__(self):
    self.setup()
    
    while self.player.hit_points and (self.monster or self.monsters):
      print('\n'+ '=' *20)
      print("{} has HP: {} and XP: {}".format(self.player.name, self.player.hit_points, self.player.experience))
      print('\n'+ '-' *20)
      self.monster_turn()
      self.player_turn()
      self.clean_up()
    
    if self.player.hit_points:
      print("You win")
    elif self.monster or self.monsters:
      print("You lose")
    sys.exit()
             
Game()