""" This code automaticly play with dice and player with most attempts win"""

from random import randrange

for player in range(1, 5 ):
    
    attempt_numb = 0
    print("Hraje hráč č.", player)   

    while True:
        
        dice = randrange(1, 7)
        attempt_numb += 1
        print("Hodil jsi", dice)
        if dice == 6:
            break      
             

    if player == 1:
        winner = player
        win_points = attempt_numb
    
    if attempt_numb > win_points:
        winner = player
        win_points = attempt_numb


    print("Počet tvých pokusů:", attempt_numb)
    print()


print("Vyhrává hráč č.: ", winner)