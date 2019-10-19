
from random import randrange

# List of variables needed
outcome = ''
outcome_binary = 0
player_count = int(input('Enter the number of players playing(2 to 4): '))
player_1 = input('Enter name of Player_1: ')
player_2 = input('Enter name of player_2: ')
player_picker = randrange(player_count)
player_chosen = ''
input_to_continue = 'y'
outcome_binary = randrange(2)

# Player count and name allocation.
if player_count == 3:
    player_3 = input('Enter name of player_3: ')
    
elif player_count == 4:
    player_3 = input('Enter name of player_3: ')
    player_4 = input('Enter name of player_4: ')
else:
    pass

if player_picker == 0:
    player_chosen = player_1
    
elif player_picker == 1:
    player_chosen = player_2
    
elif player_picker == 2:
    player_chosen = player_3
    
elif player_picker == 3:
    player_chosen = player_4
    

print('The player chosen is ' + player_chosen)
print()


input_user = (input('Type Y to continue! \n').lower())
if input_to_continue == input_user:
    if outcome_binary %2 == 0:
        outcome = 'Truth'
    else:
        outcome = 'Dare'
        
# Used "" as there is ' in It's
print(player_chosen, "It's time for a ", outcome)

