import random

MAP = [(0,0), (0,1), (0,2),
       (1,0), (1,1), (1,2),
       (2,0), (2,1), (2,2),]

def get_locations():
  
  monster = random.choice(MAP)
  door = random.choice(MAP)
  player = random.choice(MAP)
  
  if monster == door or player == door or player == monster:
    return get_locations()
  
  return monster, door, player    

def move_player(move, player):
  
  if move == 'LEFT':
    player = (player[0],player[1]-1) 
  elif move == 'UP':
    player = (player[0]-1,player[1]) 
  elif move == 'DOWN':
    player = (player[0]+1,player[1]) 
  else:
    player = (player[0],player[1]+1) 
  return player

def get_moves(player):
  moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  
  if player[1] == 0:
    moves.remove('LEFT')
  if player[1] == 2:
    moves.remove('RIGHT')
  if player[0] == 0:
    moves.remove('UP')
  if player[0] == 2:
    moves.remove('DOWN')
  
  return moves

def draw_map(player, door):
  print(" _ _ _ ")
  title = "|{}"
  
  for index, cell in enumerate(MAP):
    if index in {0, 1, 3, 4, 6, 7}:
      if cell == player:
        print(title.format("X"), end='')
      else:
        print(title.format("_"), end='')
    else:
      if cell == player:
        print(title.format("X|"))
      else:
        print(title.format("_|"))

monster, door, player = get_locations()
moves = []

while True:
  moves = get_moves(player)
  print("Welcome to the dungeon")
  print("you're currently in room {}".format(player)) # fill in format with player position
  
  draw_map(player, door)
  
  print("You can move {}".format(moves)) #fill in with available moves
  print("Enter Q to quit")
  
  move = input(">")
  move = move.upper()
  
  if (move == 'Q'):
    print("you have quit the game")    
    break
  if (move not in moves):
    print("Incorrect move please choose {}".format(moves))
    continue
  else:
    player = move_player(move, player)
    
  if player == monster:
    print("You have gotten caught by the monster")
    break
  elif player == door:
    print("You made it")
    break
  
  
  