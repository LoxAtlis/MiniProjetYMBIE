WIDTH = 800
HEIGHT = 600

bg1 = Actor("bg1")
bg1.pos = [400,300]

player = Actor("player")
player.pos = [400,300]



def draw():
    screen.clear()
    bg1.draw()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0],player.pos[1]]