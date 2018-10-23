import random

koszyczek = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ]


def generujTeamy(lista):
    random.shuffle(lista)
    polowa = len(koszyczek)//2
    team1 = koszyczek[0:]
    team2 = koszyczek[polowa : ]
    print(team1)
    print (team2)

    return team1, team2

print ('wynik funkcji to: ',generujTeamy( [1,2,3,4,5,6,7,8,9,0] ))
print ('Typ wyniku to: ',type(generujTeamy( [1,2,3,4,5,6,7,8,9,0] )))