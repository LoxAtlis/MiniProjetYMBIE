WIDTH = 800
HEIGHT = 600

LEFT = 1
RIGHT = 3

# bg1 = Actor("bg1")
# bg1.pos = [400,300]

player = Actor("player")
player.pos = [400,550]

bullet = Actor("projectile")
bullet.pos = player.pos
bullet_speed = [0, -4]

def draw():
    screen.clear()

    # bg1.draw()
    player.draw()
    bullet.draw()

def on_mouse_move(pos):
    player.pos = [pos[0],player.pos[1]]

#click droit ou gauche
def on_mouse_down(button):
    if button == LEFT or button == RIGHT:
        print("HELLO")

#fonction pour tirer une bullete
#def shoot():
	#bullet = Actor("projectile")
	#bullet.pos = player.pos

def update():
    global bullet
    global bullet_speed
    new_x = bullet.pos[0] + bullet_speed[0] # new_x = position de la bullete + vitesse de la bullete (3)
    new_y = bullet.pos[1] + bullet_speed[1] # new_y = position de la bullete + vitesse de la bullete (-3)
    bullet.pos = [new_x, new_y]