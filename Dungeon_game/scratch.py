#class Game:
#  def __init__(self):
#    self.current_score = [0, 0]
#    
#    player = input("Enter player's value: ")
#      
#  def score(self, player):
#    self.player = player
#    if self.player == '1':
#      new_score = self.current_score[0] + 1
#      return new_score
#    
#    if self.player == '2':
#      new_score = self.current_score[1] + 1
#      return new_score

  def player_turn():
    player_choice = input("[A]ttack, [R]est, [Q]uit").lower()
    if player_choice == 'a':
      print("You are attacking {}".format(self.monster))
      if self.player.attack():
        if self.monster.dodge():
          print("{} has dodged this attack".format(self.monster))
        else:
          if self.level_up():
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
      
        
    if player_choice =='a':
      if self.player.attack():
        if self.monster.dodge():
          print("{} has dodged this attack".format(self.monster)
        else:
          if self.level_up():
            self.monster.hit_points -= 2
          else:
            self.monster.hit_points -= 1   
         print("{} has hit {} with a {}".format(self.player.name, self.monster, self.player.weapon)
      else:
        print("{} does not want to attack".format(self.player.name)
     elif player_choice == 'r':
       self.player.rest()
     elif player_choice == 'q':
       sys.exit()
              
              
 def monster_turn(self):
    if self.monster.attack():
      print("Attack has been initiated by {}".format(self.monster))
      dodge = input("Would you like to dodge the attack,(Y/N)").lower()
      if dodge.lower == 'y':
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
              
  
              