WIDTH = 800
HEIGHT = 600

LEFT = 1
RIGHT = 3
loose = False

player = Actor("player")
player.pos = [400,550]

bullet = Actor("bullet")
bullet.pos = player.pos
bullet_speed = [0, -15]

ennemy = Actor("ennemy")
ennemy.pos = [400, 300]

gameover = Actor("go-im")

def draw():
    screen.clear()
    bullet.draw()
    player.draw()
    ennemy.draw()

    if loose:
        gameover.draw()

def on_mouse_move(pos):
    player.pos = [pos[0],player.pos[1]]

#click droit ou gauche
def on_mouse_down(button):
    if button == LEFT or button == RIGHT:
        shoot()

#fonction pour tirer une bullet
def shoot():
	bullet.pos = player.pos

def update():
    global bullet
    global bullet_speed
    new_x = bullet.pos[0] + bullet_speed[0]
    new_y = bullet.pos[1] + bullet_speed[1]
    bullet.pos = [new_x, new_y]

# ATTENTION Il faut adapeter le code si on utilise une liste pour les ennemies
    if bullet.colliderect(ennemy):
        ennemy.remove()

    # if (ennemy.bottom > HEIGHT or ennemy.colliderect(player)) and not loose:
	#     loose = True