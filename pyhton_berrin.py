# Pyhton file by Berrin 

# Ennemie position aleatoire en haut

from random import randint

WIDTH = 800
HEIGHT = 600

all_ennemie = []

# Placer les Ennemies
def setup_ennemie():
    global all_ennemie
    
    for x in range (0, 800, 100):
        for y in range(0, 30, 30):
            ennemie = Actor("brick-perso", anchor=["left", "top"]) 
            ennemie.pos = [x, y]
            all_ennemie.append(ennemie)
setup_ennemie()

def draw():
    global all_ennemie

    screen.clear()
    # bg1.draw()
    # player.draw()

    for ennemie in all_ennemie:
        ennemie.draw()