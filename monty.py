import random
import sys

#Play the game 
def monty_hall_game(switch, doors = [0,1,2]):
  num_doors = len(doors) #Get the number of doors

  #randomly chosen prize door, from 1 to the number of doors
  prize_door = random.randint(0, num_doors-1)
  #Initializes with a random choice out of the three doors.
  player_choice = random.randint(0, num_doors-1)
  #host shows all but one remaining doors, excluding your choice.
  shown_doors = list(range(num_doors))
  shown_doors.remove(player_choice)

  #tries to remove the prize door if you didn't already choose it
  if prize_door in shown_doors:
    shown_doors.remove(prize_door)
    door_not_shown = prize_door
  #if you did choose it, then it just removes a different random door.
  else:
    door_not_shown = random.choice(shown_doors)
    shown_doors.remove(door_not_shown)
  #if you chose to switch, here's where you'd do it.
  if switch:
    player_choice = door_not_shown
  #returns true if player chose the correct door, otherwise false.
  return player_choice == prize_door

doors = list(range(int(sys.argv[1])))

num_trials = int(sys.argv[2])

w_switch = sum([monty_hall_game(True, doors) for i in range(num_trials)])
w_no_switch = sum([monty_hall_game(False, doors) for i in range(num_trials)])

print('Trial 1 with switching:')
print(f'Win switch %: {w_switch/ num_trials}')
print(f'Lose switch %: {(num_trials - w_switch) / num_trials}')
print('Trial 2 without switching:')
print(f'Win with no switch %: {w_no_switch/ num_trials}')
print(f'Lose with no switch %: {(num_trials - w_no_switch) / num_trials}')