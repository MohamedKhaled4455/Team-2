# import important libraries
import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GREY = (100, 100, 100)
BLUE = (0, 51, 102)

# coordinates for movement
x = 0
y = 0
z = [x, y]

# This indicates the (WIDTH) and (HEIGHT) of each grid location
WIDTH = 66
HEIGHT = 66

# This sets the margin between each cell
MARGIN = 1

# randomize movement of rat
Rx = [137, 203, 269, 335, 401]
Ry = [137, 203, 269, 335, 401]
R_mouse = [137, 203, 269, 335, 401, 71, 467]
r_catx = random.choice(Rx)
r_caty = random.choice(Ry)
r_catv = (r_catx, r_caty)
r_mousex = random.choice(Rx)
r_mousey = random.choice(Ry)
mouse_pos_x = random.choice(Rx)
mouse_pos_y = random.choice(Ry)
current_pos = (mouse_pos_x, mouse_pos_y)

# display screen mode to certain size
Screen = pygame.display.set_mode([500, 500])
win = pygame.display
win.set_caption('Window')
surface = win.set_mode(z)

# changing rat and cat shapes by loading some images
mouse = pygame.image.load("RAT.jpg").convert_alpha()
mouse = pygame.transform.scale(mouse, (60, 60))
cat = pygame.image.load("CAT.jpg").convert_alpha()
cat = pygame.transform.scale(cat, (60, 60))

# MOVEMENT BY ARROWS
LEFT_presses = 0
right_presses = 0
UP_presses = 0
DOWN_presses = 0
KEY_LIST = [[66, 0], [-66, 0], [0, -66], [0, 66]]
way = random.randint(0, 1)

# Creation of 2 dimensional list (2D list):
grid = []
for row in range(7):
    # Add an empty array that will hold each cell in this row
    grid.append([])
    for column in range(7):
        grid[row].append([])  # Append a cell

# Initializing our engine
pygame.init()

# editing window and clock setting
WINDOW_SIZE = [600, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mouse Escaping Game")
done = False
window = True
clock = pygame.time.Clock()


# Font and size function
def font_setting(text, font):
    textsurface = font.render(text, True, GREY)
    return textsurface, textsurface.get_rect()


# CREATE A FUNCTION TO MAKE MESSAGES APPEAR ON SCREEN
def message(text):
    largetext = pygame.font.Font('freesansbold.ttf', 40)
    textsurf, textrect = font_setting(text, largetext)
    textrect.center = ((600 / 2), (600 / 2))
    screen.blit(textsurf, textrect)
    pygame.display.update()


# when die from starving
def starve():
    message('MAY SOMEONE HELP U ANOTHER TIME')


# when escapes and win
def escape():
    message('CONGRATS,U ESCAPED')


# when drowning in water
def water():
    message("mmmm, U DROWNED")


# when cat get rat
def dead():
    message("BE CAREFUL!! BLIND")


# FUNCTION DESCRIBES THE MOVEMENT OF RAT
def RAT_MOVEMENT():
    i, j = random.choice(KEY_LIST)
    global current_pos, mouse_pos_y, mouse_pos_x
    mouse_pos_y += j
    mouse_pos_x += i
    current_pos = (mouse_pos_x, mouse_pos_y)


# movement of by arrows
def keys():
    message("Move the mouse using the arrows")


# ******************** GAME LOOP ********************

while not done:
    if way == 0:
        time.sleep(0.5)
        RAT_MOVEMENT()
    for event in pygame.event.get():

        # If close button clicked
        if event.type == pygame.QUIT:
            # EXIT OUR LOOP
            done = True
        key = pygame.key.get_pressed()

        # CONTROlING BY KEYS
        if key[pygame.K_LEFT] and way == 1:
            mouse_pos_x = mouse_pos_x - 66
            current_pos = (mouse_pos_x, mouse_pos_y)
            LEFT_presses += 1
        if key[pygame.K_RIGHT] and way == 1:
            mouse_pos_x = mouse_pos_x + 66
            current_pos = (mouse_pos_x, mouse_pos_y)
            right_presses += 1
        if key[pygame.K_UP] and way == 1:
            mouse_pos_y = mouse_pos_y - 66
            current_po_s = (mouse_pos_x, mouse_pos_y)
            UP_presses += 1
        if key[pygame.K_DOWN] and way == 1:
            mouse_pos_y = mouse_pos_y + 66
            current_pos = (mouse_pos_x, mouse_pos_y)
            DOWN_presses += 1
    KEY_PRESSES = LEFT_presses + right_presses + UP_presses + DOWN_presses

    # ALL SCENARIOS THAT MAY HAPPEN
    # (I) WHEN MOVE MORE THAN 20 STEPS
    if KEY_PRESSES == 21:
        starve()
        time.sleep(2)
        exit()

    # (II) WHEN FINALLY ESCAPES FROM CAT
    if current_pos == (467, 269):
        escape()
        time.sleep(2)
        exit()

    # (III) When drowned (touches the water)
    if (mouse_pos_y == 71 or mouse_pos_y == 467) and (mouse_pos_x in R_mouse):
        water()
        time.sleep(2)
        exit()
    if (mouse_pos_x == 71 or mouse_pos_x == 467) and (mouse_pos_y in R_mouse):
        water()
        time.sleep(2)
        exit()

    # (IV) When touching the cat
    if current_pos == r_catv:
        dead()
        time.sleep(1)
        exit()
    surface.blit(cat, (r_catx, r_caty))  # Displaying cat and mouse
    surface.blit(mouse, current_pos)
    win.update()
    pygame.display.update()
    screen.fill(BLACK)

    # Drawing our grid
    for row in range(1):
        for column in range(7):
            color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 66,
                              (MARGIN + HEIGHT) * row + MARGIN + 66,
                              WIDTH,
                              HEIGHT])
    for row in range(7):
        for column in range(1):
            color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 66,
                              (MARGIN + HEIGHT) * row + MARGIN + 66,
                              WIDTH,
                              HEIGHT])
    for row in range(7):
        for column in range(1):
            color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 468,
                              (MARGIN + HEIGHT) * row + MARGIN + 66,
                              WIDTH,
                              HEIGHT])
    for row in range(1):
        for column in range(7):
            color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 66,
                              (MARGIN + HEIGHT) * row + MARGIN + 468,
                              WIDTH,
                              HEIGHT])
    for row in range(5):
        for column in range(5):
            color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 133,
                              (MARGIN + HEIGHT) * row + MARGIN + 133,
                              WIDTH,
                              HEIGHT])
    for row in range(1):
        for column in range(1):
            color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 468,
                              (MARGIN + HEIGHT) * row + MARGIN + 266,
                              WIDTH,
                              HEIGHT])
    clock.tick(300)

# QUIT OUR GAME
pygame.quit()
