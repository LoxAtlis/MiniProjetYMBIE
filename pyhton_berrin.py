# Pyhton file by Berrin 

# Ennemie position aleatoire en haut
from random import randint, random

WIDTH = 800
HEIGHT = 600

all_ennemy = []
ennemy_speed = [0, 3]

game_over = 0

# Placer les Ennemies en haut en dehors de la fenetre 
def setup_ennemy():
    global all_ennemy
    global game_over

    while game_over < 4 :

        game_over = game_over + 1
        random_number = randint(100,200)

        for x in range (0,800, random_number):           # debut, fin, espacement
            print(randint(1, 800))
            for y in range(0, 50, random_number):          # changez parraport au assest ennemie (grandeur largeurs etc? ?? 


                ennemy = Actor("ennemy", anchor=["left", "top"]) 
                ennemy.pos = [x, y]
                all_ennemy.append(ennemy)
            
setup_ennemy()

def draw():
    global all_ennemy

    screen.clear()
    # bg1.draw()
    # player.draw()

    for ennemy in all_ennemy:
        ennemy.draw()

def update(dt):

     # move down  
    for ennemy in all_ennemy:
        new_x = ennemy.pos[0] + ennemy_speed[0]
        new_y = ennemy.pos[1] + ennemy_speed[1]

        ennemy.pos = [new_x, new_y]


    # # check boundries
    # if ball.right >= WIDTH or ball.left <= 0:  # ball.right, donne la 
    #                                         # position a droit de la ball
    #     invert_horizontal_speed()


# score = 0

# def draw():
#     showing_score()

# def showing_score():
#     global ball_fall_count

#     if ball_fall_count == 3:
#         screen.draw.text("score: " + str(score), midtop=(400, 350), owidth=1.5, ocolor=("purple"), color="pink")

#         all_bricks = []

#     else:
#         screen.draw.text("score: " + str(score), bottomright=(790, 599), owidth=1.5, ocolor=("purple"), color="pink")

# def update(dt):
#     global score 

# score =  score + 10 # placer achaque ennemie touché 