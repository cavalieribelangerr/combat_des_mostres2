# Romain
# combat_des_monstres2

import random
jouer = True
numMonstre = 0
nb = 0
nbV = 0
nbD = 0
playerVie = 20
nb_consecutive = 0
while jouer:

    playerForce = random.randint(0, 20)
    monstreForce = random.randint(0, 20)
    print('Vous tombez face à face avec un adversaire de difficulté :', monstreForce)
    choix = int(input(print('''Que voulez-vous faire ? 
	1- Combattre cet adversaire
	2- Contourner cet adversaire et aller ouvrir une autre porte
	3- Afficher les règles du jeu
	4- Quitter la partie
	
	''')))
    if nb_consecutive == 3:
        print('VOTRE ADVERSAIRE EST UN BOSS, IL SERA DONC PLUS FORT')
        monstreForce = random.randint(12, 20)

    if choix == 1:
        numMonstre += 1
        print('''Adversaire :''', numMonstre,
        '''Force de l’adversaire :''',monstreForce,
        '''Niveau de vie de l’usager :''', playerVie,
        '''Combat ''',nb,''' : ''',nbV,'''vs''', nbD)
        print('''
        
        Lancer du dé : ''', playerForce)

        if monstreForce > playerForce:
            nb += 1
            nbD += 1
            playerVie -= monstreForce
            print('Dernier combat = Défaite' )
            print('''Niveau de vie : ''', playerVie)
            if playerVie <= 0:
                print('La partie est terminée, vous avez vaincu', nbV, ' monstre(s).')
                jouer = False

            nb_consecutive = 0
        elif monstreForce < playerForce:
            nb += 1
            nbV += 1

            print('Dernier combat =Victoire' )
            print('Vie = ', playerVie)
            nb_consecutive += 1
    elif choix == 2:
        playerVie -= 1

    elif choix == 3:
        print('''Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.


La partie se termine lorsque les points de vie de l’usager tombent sous 0.


L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
''')

    elif choix == 4:
        print('Merci! au revoir...')
        jouer = False