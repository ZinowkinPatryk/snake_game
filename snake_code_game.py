import pygame
import random
import sys


def random_blocs_of_points():
    global snake_body_position
    random_ = [random.choice(range(0, 690, 10)), random.choice(range(0, 480, 10))]
    if random_ in snake_body_position:
        random_blocs_of_points()
    return random_


def it_eaten(updown_move, leftright_move, random_):
    if abs(leftright_move - random_[0]) < 40 and abs(updown_move - random_[1]) < 40:
        return True
    return False


def is_hitting_wall_or_nail():
    global up_down_move, left_right_move, snake_body_position
    if len(snake_body_position) > 3:
        head = snake_body_position[0]
        for i in snake_body_position[3:]:
            if i == head:
                return True
    if up_down_move < 0 or up_down_move > 490 or left_right_move < 0 or left_right_move > 690:
        return True
    return False


def moving(ev):
    global current_key
    if ev.key == pygame.K_w:
        if current_key[0] == "s":
            return 1
        current_key[0] = "w"
        return 0
    elif ev.key == pygame.K_s:
        if current_key[0] == "w":
            return 0
        current_key[0] = "s"
        return 1
    elif ev.key == pygame.K_a:
        if current_key[0] == "d":
            return 3
        current_key[0] = "a"
        return 2
    elif ev.key == pygame.K_d:
        if current_key[0] == "a":
            return 2
        current_key[0] = "d"
        return 3
    else:
        if current_key[0] == "w":
            return 0
        if current_key[0] == "s":
            return 1
        if current_key[0] == "a":
            return 2
        if current_key[0] == "d":
            return 3


def draw_snake_eyes(position, key):

    snake_head_x = position[0]
    snake_head_y = position[1]
    eye_radius = 5
    pupil_radius = 2
    eye_offset_x = 12
    eye_offset_y = 12

    if key == ['w']:
        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + eye_offset_x, snake_head_y + eye_offset_y),
                           eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + eye_offset_x, snake_head_y + eye_offset_y), pupil_radius)
        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + 28, snake_head_y + eye_offset_y), eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + 28, snake_head_y + eye_offset_y), pupil_radius)
    elif key == ['s']:
        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + eye_offset_x, snake_head_y + eye_offset_y + 12),
                           eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + eye_offset_x, snake_head_y + eye_offset_y + 12),
                           pupil_radius)
        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + 28, snake_head_y + eye_offset_y + 12),
                           eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + 28, snake_head_y + eye_offset_y + 12), pupil_radius)
    elif key == ['a']:

        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + eye_offset_x, snake_head_y + eye_offset_y + 15),
                           eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + eye_offset_x, snake_head_y + eye_offset_y + 15),
                           pupil_radius)
        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + 12, snake_head_y + eye_offset_y), eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + 12, snake_head_y + eye_offset_y), pupil_radius)
    elif key == ['d']:
        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + eye_offset_x + 12, snake_head_y + eye_offset_y),
                           eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + eye_offset_x + 12, snake_head_y + eye_offset_y),
                           pupil_radius)

        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + 24, snake_head_y + eye_offset_y + 15), eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + 24, snake_head_y + eye_offset_y + 15), pupil_radius)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + eye_offset_x, snake_head_y + eye_offset_y),
                           eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + eye_offset_x, snake_head_y + eye_offset_y), pupil_radius)
        pygame.draw.circle(screen, (255, 255, 255), (snake_head_x + 28, snake_head_y + eye_offset_y), eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (snake_head_x + 28, snake_head_y + eye_offset_y), pupil_radius)


def add_new_position(up_down, left_right):
    global snake_body_position, long_snake
    if len(snake_body_position) == len(long_snake):
        snake_body_position.insert(0, snake_body_position.pop())
        snake_body_position[0] = [left_right, up_down]
    else:
        snake_body_position = [[left_right, up_down]] + snake_body_position


def draw_snake(postition):
    global current_key
    for i in range(0, len(postition)):
        if i == 0:
            if current_key[0] == "w":
                pygame.draw.rect(screen, (11, 252, 3), (postition[0][0], postition[0][1], 40, 40),
                                 border_top_left_radius=10, border_top_right_radius=10)
            elif current_key[0] == "s":
                pygame.draw.rect(screen, (11, 252, 3), (postition[0][0], postition[0][1], 40, 40),
                                 border_bottom_left_radius=10, border_bottom_right_radius=10)
            elif current_key[0] == "a":
                pygame.draw.rect(screen, (11, 252, 3), (postition[0][0], postition[0][1], 40, 40),
                                 border_top_left_radius=10, border_bottom_left_radius=10)
            elif current_key[0] == "d":
                pygame.draw.rect(screen, (11, 252, 3), (postition[0][0], postition[0][1], 40, 40),
                                 border_top_right_radius=10, border_bottom_right_radius=10)
        elif i == len(postition)-1:
            if current_key[0] == "w":
                pygame.draw.rect(screen, (11, 252, 3), (postition[i][0], postition[i][1], 40, 40),
                                 border_bottom_left_radius=10, border_bottom_right_radius=10)
            elif current_key[0] == "s":
                pygame.draw.rect(screen, (11, 252, 3), (postition[i][0], postition[i][1], 40, 40),
                                 border_top_left_radius=10, border_top_right_radius=10)
            elif current_key[0] == "a":
                pygame.draw.rect(screen, (11, 252, 3), (postition[i][0], postition[i][1], 40, 40),
                                 border_bottom_right_radius=10, border_top_right_radius=10)
            elif current_key[0] == "d":
                pygame.draw.rect(screen, (11, 252, 3), (postition[i][0], postition[i][1], 40, 40),
                                 border_bottom_left_radius=10, border_top_left_radius=10)
        else:
            pygame.draw.rect(screen, (11, 252, 3), (postition[i][0], postition[i][1], 40, 40))
        draw_snake_eyes(postition[0], current_key)


def pause():
    global snake_body_position, long_snake, left_right_move, up_down_move, value_move, counter_score, game_over, \
        points_font, mute_counter
    paused = True
    # silenced
    silenced = pygame.image.load("texture\\coins\\silenced.png")
    silenced = pygame.transform.scale(silenced, (40, 40))

    # mute
    mute = pygame.image.load("texture\\coins\\MUTE.png")
    mute = pygame.transform.scale(mute, (45, 45))

    button_sound = pygame.Rect(10, 665, 50, 50)
    # button NEW GAME and QUIT
    fontt = pygame.font.SysFont('Arial', 30)
    text1 = fontt.render("New game", True, (0, 0, 0))
    text2 = fontt.render("Quit", True, (0, 0, 0))
    button_width, button_height = 150, 50
    button1_rect = pygame.Rect(720 // 2 - button_width - 10, 250, button_width,
                               button_height)
    button2_rect = pygame.Rect(720 // 2 + 10, 250, button_width, button_height)
    # PAUSED GAME
    while paused:
        pygame.draw.rect(screen, (200, 200, 200), (10, 665, 50, 50), border_radius=5)
        if mute_counter == 0:
            pygame.mixer.music.unpause()
            screen.blit(silenced, (13, 668))
        else:
            pygame.mixer.music.pause()
            screen.blit(mute, (13, 668))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(ev.pos):
                    if mute_counter == 0:
                        pygame.mixer.music.play(-1)
                    pygame.display.flip()
                    screen.blit(background, (0, 0))
                    long_snake = [0, ]
                    up_down_move = 350
                    left_right_move = 350
                    counter_score = 0
                    screen.blit(nd_background, (-10, 530))
                    screen.blit(score_baner, (230, 550))
                    screen.blit(background, (0, 0))
                    points_font = font.render(str(counter_score), True, (255, 255, 255))
                    snake_body_position = [[left_right_move, up_down_move], ]
                    value_move = -2
                    pygame.draw.rect(screen, (11, 252, 3),
                                     (snake_body_position[0][0], snake_body_position[0][1], 40, 40),
                                     border_top_left_radius=10, border_top_right_radius=10)
                    pygame.time.delay(30)
                    pygame.display.flip()
                    return None
                elif button2_rect.collidepoint(ev.pos):
                    pygame.quit()
                    sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if button_sound.collidepoint(ev.pos):
                    if mute_counter == 0:
                        mute_counter = 1
                    else:
                        mute_counter = 0
        draw_snake(snake_body_position)
        pygame.draw.rect(screen, (200, 200, 200), button1_rect, border_radius=10)
        pygame.draw.rect(screen, (200, 200, 200), button2_rect, border_radius=10)
        screen.blit(text1, (button1_rect.x + 2, button1_rect.y + 10))
        screen.blit(text2, (button2_rect.x + 40, button2_rect.y + 10))
        pygame.display.flip()


def draw(val_mov):
    global up_down_move, left_right_move, random_position, counter_score, points_font, long_snake, \
        snake_body_position, current_key, mute_counter
    screen.blit(points_font, (339, 600))
    if val_mov == -2:    # BEGINNING, any button (WASD) wasn't clicked
        draw_snake(snake_body_position)
        pygame.display.flip()
    if val_mov == 0:     # W
        current_key = ["w"]
        up_down_move -= 10
        add_new_position(up_down_move, left_right_move)
        screen.blit(background, (0, 0))
        draw_snake(snake_body_position)
        pygame.display.flip()
    if val_mov == 1:     # S
        current_key = ["s"]
        up_down_move += 10
        add_new_position(up_down_move, left_right_move)
        screen.blit(background, (0, 0))
        draw_snake(snake_body_position)
        pygame.display.flip()
    if val_mov == 2:     # A
        current_key = ["a"]
        left_right_move -= 10
        add_new_position(up_down_move, left_right_move)
        screen.blit(background, (0, 0))
        draw_snake(snake_body_position)
        pygame.display.flip()
    if val_mov == 3:     # D
        current_key = ["d"]
        left_right_move += 10
        add_new_position(up_down_move, left_right_move)
        screen.blit(background, (0, 0))
        draw_snake(snake_body_position)
        pygame.display.flip()

    if it_eaten(up_down_move, left_right_move, random_position):
        if mute_counter == 0:
            eating_sound.play()
        counter_score += 1
        long_snake.append(len(long_snake))
        screen.blit(score_baner, (230, 550))
        points_font = font.render(str(counter_score), True, (255, 255, 255))
        random_position = random_blocs_of_points()
        add_new_position(up_down_move, left_right_move)
        draw_snake(snake_body_position)
        pygame.time.delay(45)
        pygame.display.flip()
    else:
        screen.blit(apple, (random_position[0], random_position[1]))
        pygame.display.flip()
        pygame.time.delay(45)


# variables
current_key = [""]
counter_score = 0
run = True
value_move = -2
up_down_move = 350
left_right_move = 350
snake_body_position = [[left_right_move, up_down_move]]
long_snake = [0, ]
random_position = random_blocs_of_points()
mute_counter = 0
# window

pygame.init()
dimension = [720, 720]
screen = pygame.display.set_mode((dimension[0], dimension[0]))
pygame.display.set_caption("SNAKE_BY_CZECZEN")

# text
font = pygame.font.SysFont('Arial', 35)
points_font = font.render(str(counter_score), True,  (255, 255, 255))
game_over = font.render("GAME OVER", True, (255, 255, 255))

# LOGO
logo = pygame.image.load("texture\\logo_icons\\logo.png")

# background
background = pygame.image.load("texture\\backgrounds\\background_texture.png")
background = pygame.transform.scale(background, (720, 532))
score_baner = pygame.image.load("texture\\backgrounds\\score_baner_texture.png").convert_alpha()
score_baner = pygame.transform.scale(score_baner, (270, 120))
nd_background = pygame.image.load("texture\\backgrounds\\2backgraund.png")
nd_background = pygame.transform.scale(nd_background, (730, 500))

# apple
apple = pygame.image.load("texture\\coins\\apple_texture.png")
apple = pygame.transform.scale(apple, (40, 40))


# sound
pygame.mixer.init()
eating_sound = pygame.mixer.Sound("sound\\eating_sound.mp3")
hit_sound = pygame.mixer.Sound("sound\\hit_sound.mp3")
game_over_sound = pygame.mixer.Sound("sound\\game_over.mp3")
pygame.mixer.music.load("sound\\background_music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


# MAP OUTLINE
screen.blit(nd_background, (-10, 530))
screen.blit(background, (0, 0))
screen.blit(score_baner, (230, 550))
pygame.draw.rect(screen, (11, 252, 3), (snake_body_position[0][0], snake_body_position[0][1], 40, 40),
                 border_top_left_radius=10, border_top_right_radius=10)

# MAIN LOOP
screen.blit(logo, (210, 60))
pause()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            value_move = moving(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause()
    if is_hitting_wall_or_nail():
        if mute_counter == 0:
            pygame.mixer.music.stop()
            hit_sound.play()
            pygame.time.delay(2750)
            screen.blit(game_over, (260, 190))
            game_over_sound.play()
            pygame.time.delay(1000)
            pause()
        else:
            screen.blit(game_over, (260, 190))
            pygame.time.delay(1000)
            pause()
            screen.blit(background, (0, 0))
    draw(value_move)
