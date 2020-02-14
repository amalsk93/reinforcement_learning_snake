import random
import pygame

width = 500
cell_size = 25
flag = True
recook_snack = True
win = pygame.display.set_mode((width, width))
clock = pygame.time.Clock()


class Cube():
    def __init__(self, color=(255, 0, 0), size=cell_size, pos=None):
        self.dirnx = 1
        self.dirny = 1
        if pos is None:
            pos = [250, 225]
        self.color = color
        self.size = size
        self.pos = pos

    def create_cube(self, surf, dx=1, dy=1):
        x = self.pos[0]
        y = self.pos[1]
        print(x, y)
        pygame.draw.rect(surf, self.color, (x, y, dx * self.size, dy * self.size))

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def move_snake(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


class Snake(Cube):
    def __init__(self, body=None, color=(0, 0, 255), size=cell_size, pos=None):
        self.head = Cube(color=color, pos=pos)
        self.body = []
        self.body.append(self.head)
        super().__init__(color, size, pos)

    def eat_snack(self):
        global recook_snack
        tail = self.body[-1]
        # dx, dy = tail.dirnx, tail.dirny
        # if dx == 1 and dy == 0:
        #     self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        # elif dx == -1 and dy == 0:
        #     self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        # elif dx == 0 and dy == 1:
        #     self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        # elif dx == 0 and dy == -1:
        #     self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))
        #
        # self.body[-1].dirnx = dx
        # self.body[-1].dirny = dy
        recook_snack = True
        self.body.append(Cube(color=(0, 0, 255), pos=[tail.pos[0], tail.pos[1] - cell_size]))


def draw_grids(wid=width, size=cell_size):
    xpos = 0
    for i in range(0, wid, size):
        xpos = xpos + i
        pygame.draw.line(win, (0, 0, 0), (i, 0), (i, wid), 1)
        pygame.draw.line(win, (0, 0, 0), (0, i), (wid, i), 1)


def generate_snack_cube(cube_obj, surf, wid=width):
    global recook_snack
    if recook_snack:
        x_pos = random.randrange(0, wid, cube_obj.size)
        y_pos = random.randrange(0, wid, cube_obj.size)
        # x_pos, y_pos = 250, 225
        cube_obj.pos = [x_pos, y_pos]
    cube_obj.create_cube(surf)
    recook_snack = False

snake = Snake()
snack = Cube()
while flag:
    win.fill((255, 255, 255))
    draw_grids()
    generate_snack_cube(snack, win)
    pygame.time.delay(50)
    clock.tick(10)

    for i in snake.body:
        i.create_cube(win, dx=snake.body[-1].dirnx, dy=snake.body[-1].dirny)
        if i.pos[1] < width:
            i.pos[1] = i.pos[1] + cell_size
        else:
            i.pos[1] = 0

    if snake.body[0].pos == snack.pos:
        snake.eat_snack()
        # print(snake.body[-1].dirnx)
    pygame.display.update()
    snack.move_snake()
