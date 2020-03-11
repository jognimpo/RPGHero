from Hero import *

def switch(turn):
    if turn == 0:
        turn = 1
        notturn = 0
    else:
        turn = 0
        notturn = 1
    return turn, notturn

players = []

for i in range(2):
    print("creating player", i+1)
    player = Hero()
    player.equip_all()
    players.append(player)
turn = 0
notturn = 1
while players[0].is_alive:
    print()
    print("its your turn")
    print(players[turn])
    x = players[turn].attack()
    players[notturn].defend(x)
    if players[1].is_alive == False:
        print(players[1].name, "has died")
        xp, item = players[1].die()
        players[0].add_xp(xp)
        players[0].add_to_inv(item)
        players[0].equip_all()
        print("A new chalenger approaches")
        player = Hero()
        player.equip_all()
        players[1] = player
    turn, notturn = switch(turn)
print("you have died")
