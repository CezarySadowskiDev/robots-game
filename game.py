import pygame
import sys
import random
import game_engine as ge
import overlay as ov

pygame.init()


req_points = 300
max_enemy = 90

width = 1284
height = 744

player_color = (255, 0, 0)
player_size = 20

background_color = (255, 255, 255)
border_color = (0, 0, 0)

max_left = 20
max_right = 1020
max_top = 20
max_bottom = 680

enemy_color = (0, 0, 255)
enemy_size = player_size

garbage_color = (105, 105, 105)
garbage_size = player_size

screen = pygame.display.set_mode((width, height))
white = (255, 255, 255)


level = 0
score = -100
teleport = 4

game_over = False

while not game_over:
    level += 1
    score += 100
    teleport += 1
    do_add_points = False

    if level <= 81:
        number_of_enemies = level + 9
    else:
        number_of_enemies = max_enemy

    level_over = False
    do_create_enemies = True

    player_pos = [random.randrange(20, 1020, player_size), random.randrange(20, 680, player_size)]

    enemy_pos = ge.draw_enemy_position(player_pos, player_size)
    enemy_list = [enemy_pos]

    garbage_list = []

    pygame.display.update()

    while not level_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                x = player_pos[0]
                y = player_pos[1]

                xE = enemy_pos[0]
                yE = enemy_pos[1]

                enemy_move = False

                if event.key in [pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP8, pygame.K_KP2, pygame.K_KP7,
                                 pygame.K_KP9, pygame.K_KP1, pygame.K_KP3, pygame.K_t, pygame.K_w, pygame.K_KP_MINUS]:
                    enemy_move = True
                    do_add_points = True

                if event.key == pygame.K_KP4:
                    if x - player_size < max_left:
                        enemy_move = False
                    else:
                        x -= player_size

                elif event.key == pygame.K_KP6:
                    if x + player_size > max_right:
                        enemy_move = False
                    else:
                        x += player_size

                elif event.key == pygame.K_KP8:
                    if y - player_size < max_top:
                        enemy_move = False
                    else:
                        y -= player_size

                elif event.key == pygame.K_KP2:
                    if y + player_size > max_bottom:
                        enemy_move = False
                    else:
                        y += player_size

                elif event.key == pygame.K_KP7:
                    if x - player_size < max_left or y - player_size < max_top:
                        enemy_move = False
                    else:
                        x -= player_size
                        y -= player_size

                elif event.key == pygame.K_KP9:
                    if x + player_size > max_right or y - player_size < max_top:
                        enemy_move = False
                    else:
                        x += player_size
                        y -= player_size

                elif event.key == pygame.K_KP1:
                    if x - player_size < max_left or y + player_size > max_bottom:
                        enemy_move = False
                    else:
                        x -= player_size
                        y += player_size

                elif event.key == pygame.K_KP3:
                    if x + player_size > max_right or y + player_size > max_bottom:
                        enemy_move = False
                    else:
                        x += player_size
                        y += player_size

                elif event.key in [pygame.K_t, pygame.K_KP5]:
                    if teleport <= 0:
                        enemy_move = False
                    else:
                        x, y = ge.safe_teleport(player_pos, enemy_list, player_size, garbage_list)
                        teleport -= 1

                elif event.key in [pygame.K_w, pygame.K_KP_MINUS]:
                    x = x
                    y = y

                player_pos = [x, y]

                if ge.enemy_collision_with_player(enemy_list, player_pos):
                    level_over = True
                    game_over = True
                    break

                if ge.detect_player_collision_with_garbage(player_pos, garbage_list):
                    level_over = True
                    game_over = True
                    break

                if enemy_move:
                    ge.move_enemies(enemy_list, player_pos, enemy_size)

                enemy_pos = [xE, yE]

                if ge.detect_enemy_collision_with_garbage(enemy_list, garbage_list):
                    if do_add_points:
                        score += 10

                if ge.enemy_collision_with_player(enemy_list, player_pos):
                    level_over = True
                    game_over = True
                    break

        screen.fill(background_color)
        pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

        ge.add_enemies_to_list(enemy_list, do_create_enemies, number_of_enemies, player_pos, player_size)

        ge.create_enemies(enemy_list, screen, enemy_color, enemy_size)
        if not ge.create_enemies(enemy_list, screen, enemy_color, enemy_size):
            do_create_enemies = False

        pygame.draw.polygon(screen, border_color, [(17, 17), (width - 243, 17),
                                                   (width - 243, height - 43), (17, height - 43)], 2)

        if len(enemy_list) <= 1:
            level_over = True

        ge.update_garbage_list(enemy_list, garbage_list)
        ge.make_garbage_pill(garbage_list, screen, garbage_color, garbage_size)

        ge.detect_collision_enemies(enemy_list)
        if ge.destroy_enemies(enemy_list):
            if do_add_points:
                score += 10
        if ge.detect_enemy_collision_with_garbage(enemy_list, garbage_list):
            if do_add_points:
                score += 10

        if ge.add_teleport(score, req_points):
            if level < 60:
                req_points += 300
            else:
                req_points += 600
            teleport += 1

        # menu po prawej stronie ekranu
        ov.right_menu(border_color, screen, player_color, player_size, enemy_color, enemy_size,
                      garbage_color, garbage_size)

        # MENU NA SPODZIE EKRANU
        ov.bottom_menu(screen, level, score, teleport, border_color)

        pygame.display.update()

        if ov.game_end(game_over, screen, white, width, height, border_color, player_color,
                       player_size, enemy_color, enemy_size, garbage_color, garbage_size):

            level = 0
            score = -100
            teleport = 4
            game_over = False
