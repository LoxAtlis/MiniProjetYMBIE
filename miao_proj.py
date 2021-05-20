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
for x in range (0,800, random_number):           
    for y in range(0, 50, random_number):          
        asteroid = Actor("asteroid128", anchor=["left", "top"])
        asteroid.pos = [x,y]
        asteroid_speed = [0,300]
        all_asteroid.append(asteroid)

    for x in range (200,600, random_number):           
        for y in range(0, 50, random_number):          
            asteroid_petit = Actor("asteroid64", anchor=["left", "top"])
            asteroid_petit.pos = [x,y]
            asteroid_petit_speed = [0,200]
            all_asteroid.append(asteroid_petit)

def reboot():
    global  all_asteroid
    global asteroid
    global asteroid_speed
    global asteroid_petit
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
            asteroid_petit = Actor("asteroid64", anchor=["left", "top"])
            asteroid_petit.pos = [x,y]
            asteroid_petit_speed = [0,200]
            all_asteroid.append(asteroid_petit)



    
def update_asteroid(dt):
    global  all_asteroid
    global asteroid
    global asteroid_speed
    global asteroid_petit
    global asteroid_petit_speed


    for asteroid in all_asteroid:   # (pour creer un asteroid)
        new_y = asteroid.pos[1] + asteroid_speed[1] *dt
        new_x = asteroid.pos[0] + asteroid_speed[0] *dt
        asteroid.pos = [new_x,new_y]
        #all_asteroid.append(asteroid)
    
    for asteroid_petit in all_asteroid:   # (pour creer un asteroid)
        new_y = asteroid_petit.pos[1] + asteroid_petit_speed[1] *dt
        new_x = asteroid_petit.pos[0] + asteroid_petit_speed[0] *dt
        asteroid_petit.pos = [new_x,new_y]

    if asteroid.pos[1] > 600:
        reboot()
    

def update(dt):
    update_asteroid(dt)
    
   
def draw():
    screen.clear()
    bg1.draw()
    for asteroid in all_asteroid:
        asteroid.draw()
    for asteroid_petit in all_asteroid:
        asteroid_petit.draw()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0],player.pos[1]]


