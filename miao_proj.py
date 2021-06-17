from random import randint
WIDTH = 800
HEIGHT = 600

bg1 = Actor("bg1")
bg1.pos = [400,300]

player = Actor("player")
player.pos = [400,550]


all_asteroid = []
all_Ennemy = []

# asteroid_apparition = 50
random_number = randint(400,600)
for x in range (0,800, random_number):           
    for y in range(0, 50, random_number):          
        asteroid = Actor("asteroid128", anchor=["left", "top"])
        asteroid.pos = [x,y]
        asteroid_speed = [0,300]
        all_asteroid.append(asteroid)

    for x in range (200,600, random_number):           
        for y in range(0, 50, random_number):          
            Ennemy = Actor("ennemy", anchor=["left", "top"])
            Ennemy.pos = [x,y]
            Ennemy_speed = [0,200]
            all_Ennemy.append(Ennemy)

def reboot():
    global  all_asteroid
    global asteroid
    global asteroid_speed
    global Ennemy
    global asteroid_petit_speed
    random_number = randint(400,600)
    for x in range (0,800, random_number):           
        for y in range(0, 50, random_number):          
            asteroid = Actor("asteroid128", anchor=["left", "top"])
            asteroid.pos = [x,y]
            asteroid_speed = [0,300]
            all_asteroid.append(asteroid)

    for x in range (200,600, random_number):           
        for y in range(0, 50, random_number):          
            Ennemy = Actor("ennemy", anchor=["left", "top"])
            Ennemy.pos = [x,y]
            Ennemy_speed = [0,200]
            all_Ennemy.append(Ennemy)



    
def update_asteroid(dt):
    global  all_asteroid
    global asteroid
    global asteroid_speed
    global Ennemy
    global Ennemy_speed


    for asteroid in all_asteroid:   # (pour creer un asteroid)
        new_y = asteroid.pos[1] + asteroid_speed[1] *dt
        new_x = asteroid.pos[0] + asteroid_speed[0] *dt
        asteroid.pos = [new_x,new_y]
        #all_asteroid.append(asteroid)
    
    for Ennemy in all_Ennemy:   # (pour creer un asteroid)
        new_y = Ennemy.pos[1] + Ennemy_speed[1] *dt
        new_x = Ennemy.pos[0] + Ennemy_speed[0] *dt
        Ennemy.pos = [new_x,new_y]

    if asteroid.pos[1] > 600:
        reboot()
    

    


def update(dt):
    update_asteroid(dt)
    
   
def draw():
    screen.clear()
    bg1.draw()
    for asteroid in all_asteroid:
        asteroid.draw()
    for Ennemy in all_Ennemy:
        Ennemy.draw()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0],player.pos[1]]


