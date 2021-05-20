WIDTH = 800
HEIGHT = 600

bg1 = Actor("bg1")
bg1.pos = [400,300]

player = Actor("player")
player.pos = [400,550]



asteroid = Actor("asteroid128")
asteroid.pos = [200,100]
asteroid_apparition = 50

def update(dt):

    # rotation += rotation_speed *dt

    # new_x = position[0] + speed[0] * dt
    # new_y = position[1] + speed[1] * dt

    # if new_y > bg1[1]:
    #     new_y = 0
    # elif new_y <0:
    #     new_y = bg1[1]

    # if new_x > bg1[0]:
    #     new_x = 0
    # elif new_x <0:
    #     new_x = bg1[0]
    # position = (new_x,new_y)


#         # new_x = new_x % RESOLUTION[0]
#         # new_y = new_y % RESOLUTION[1]
#         if new_y > RESOLUTION[1]:
#             new_y = 0
#         elif new_y <0:
#             new_y = RESOLUTION[1]

#         if new_x > RESOLUTION[0]:
#             new_x = 0
#         elif new_x <0:
#             new_x = RESOLUTION[0]

#         self.position = (new_x,new_y)


# class Asteroid(SpaceObject):
#     def __init__(self, position=(0,0), size = 3):
#         if size == 3:
#             super().__init__("assets/asteroid128.png", position,(64,64), 90)
#         elif size ==2:
#             super().__init__("assets/asteroid64.png", position,(32,32), 120)
#         elif size ==1:
#             super().__init__("assets/asteroid32.png", position,(16,16), 160)
#         self.speed = (-50,-70)
#         self.size = size


# def update(self, dt):
#         self.rotation += self.rotation_speed *dt

#         new_x = self.position[0] + self.speed[0] * dt
#         new_y = self.position[1] + self.speed[1] * dt

#         # new_x = new_x % RESOLUTION[0]
#         # new_y = new_y % RESOLUTION[1]
#         if new_y > RESOLUTION[1]:
#             new_y = 0
#         elif new_y <0:
#             new_y = RESOLUTION[1]

#         if new_x > RESOLUTION[0]:
#             new_x = 0
#         elif new_x <0:
#             new_x = RESOLUTION[0]

#         self.position = (new_x,new_y)

#         super().update(dt)
def draw():
    screen.clear()
    bg1.draw()
    asteroid.draw()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0],player.pos[1]]