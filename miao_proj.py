from random import randint
WIDTH = 800
HEIGHT = 600

bg1 = Actor("bg1")
bg1.pos = [400,300]

player = Actor("player")
player.pos = [400,550]


all_asteroid = []


# asteroid_apparition = 50


random_number = randint(400,600)
for x in range (0,800, random_number):           # debut, fin, espacement
    
    for y in range(0, 50, random_number):          # changez parraport au assest ennemie (grandeur largeurs a
        asteroid = Actor("asteroid128", anchor=["left", "top"])
        asteroid.pos = [x,y]
        asteroid_speed = [0,300]
        all_asteroid.append(asteroid)

    
def update_asteroid(dt):
    global  all_asteroid
    global asteroid


    for asteroid in all_asteroid:   # (pour creer un asteroid)
        new_y = asteroid.pos[1] + asteroid_speed[1] *dt
        new_x = asteroid.pos[0] + asteroid_speed[0] *dt
        asteroid.pos = [new_x,new_y]
        #all_asteroid.append(asteroid)
def update(dt):
    update_asteroid(dt)
   
def draw():
    screen.clear()
    bg1.draw()
    for asteroid in all_asteroid:
        asteroid.draw()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0],player.pos[1]]


