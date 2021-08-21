import random 

def dice_roll(): 
    diceRoll = random.randint(1,6)
    return diceRoll

def main(): 
    player1 = 0 
    player2 = 0 
    rounds = 1  
    player1wins = 0 
    player2wins = 0 
    player1name = str(input("Please enter the name of player 1:"))
    player2name = str(input("Please enter the name of player 2:"))

    while rounds != 10: 
    	print("Round" + str(rounds))
    	player1 = dice_roll()
    	player2 = dice_roll()
    	print( str(player1name) + "Roll:" + str(player1))
    	print( str(player2name) + "Roll:" + str(player2))

    	if player1 == player2: 
    		print('Draw!')
    	elif player1 > player2: 
    		player1wins = player1wins + 1 
    		print( str(player1name) + 'wins!')
    	else: 
    		player2wins = player2wins + 1 
    		print( str(player2name) + 'wins!')

    	rounds = rounds + 1 

    if player1wins == player2wins: 
    	print('Draw')

    elif player1wins > player2wins: 
    	print( str(player1name) + "Wins - Rounds Won:" + str(player1wins))
    else: 
        print( str(player2name) + "Wins - Rounds Won:" + str(player2wins))

main()

