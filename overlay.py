import pygame
import sys

pygame.init()


def game_end(game_over, screen, white, width, height, border_color, player_color,
             player_size, enemy_color, enemy_size, garbage_color, garbage_size):

    if not game_over:
        return False

    right_menu(border_color, screen, player_color, player_size, enemy_color, enemy_size,
               garbage_color, garbage_size)

    pygame.draw.polygon(screen, white, [(19, 19), (width - 244, 19), (width - 244, height - 44), (19, height - 44)])

    label_game_over = font4.render("KONIEC GRY", 5, border_color)
    screen.blit(label_game_over, (350, 190))

    label_play_again = font.render("Zagraj ponownie - R", 1, border_color)
    screen.blit(label_play_again, (150, 400))

    label_end_of_game = font.render("Zakończ grę - Q", 1, border_color)
    screen.blit(label_end_of_game, (650, 400))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True

                elif event.key == pygame.K_q:
                    sys.exit()


def right_menu(border_color, screen, player_color, player_size, enemy_color, enemy_size,
               garbage_color, garbage_size):
    # tytuł gry
    title = "ROBOTS"
    label_tit = font.render(title, 1, border_color)
    screen.blit(label_tit, (1098, 10))

    # sterowanie
    label_cont = font2.render("Sterowanie: ", 1, border_color)
    screen.blit(label_cont, (1097, 60))

    label_cont_4 = font3.render("Num 4 - lewo", 1, border_color)
    screen.blit(label_cont_4, (1050, 100))

    label_cont_6 = font3.render("Num 6 - prawo", 1, border_color)
    screen.blit(label_cont_6, (1050, 130))

    label_cont_8 = font3.render("Num 8 - góra", 1, border_color)
    screen.blit(label_cont_8, (1050, 160))

    label_cont_2 = font3.render("Num 2 - dół", 1, border_color)
    screen.blit(label_cont_2, (1050, 190))

    label_cont_7 = font3.render("Num 7 - lewy górny skos", 1, border_color)
    screen.blit(label_cont_7, (1050, 220))

    label_cont_9 = font3.render("Num 9 - prawy górny skos", 1, border_color)
    screen.blit(label_cont_9, (1050, 250))

    label_cont_1 = font3.render("Num 1 - lewy dolny skos", 1, border_color)
    screen.blit(label_cont_1, (1050, 280))

    label_cont_3 = font3.render("Num 3 - prawy dolny skos", 1, border_color)
    screen.blit(label_cont_3, (1050, 310))

    # komendy
    label_comm = font2.render("Komendy: ", 1, border_color)
    screen.blit(label_comm, (1106, 350))

    label_cont_w = font3.render("W - czekaj", 1, border_color)
    screen.blit(label_cont_w, (1050, 390))

    label_cont_t = font3.render("T - bezpieczny teleport", 1, border_color)
    screen.blit(label_cont_t, (1050, 420))

    # legenda
    label_legend = font2.render("Legenda: ", 1, border_color)
    screen.blit(label_legend, (1110, 460))

    # gracz
    pygame.draw.rect(screen, player_color, (1050, 500, player_size, player_size))
    label_player = font3.render("- gracz", 1, border_color)
    screen.blit(label_player, (1080, 498))

    # przeciwnik
    pygame.draw.rect(screen, enemy_color, (1050, 540, enemy_size, enemy_size))
    label_enemy = font3.render("- przeciwnik", 1, border_color)
    screen.blit(label_enemy, (1080, 538))

    # złom
    pygame.draw.rect(screen, garbage_color, (1050, 580, garbage_size, garbage_size))
    label_garbage = font3.render("- złom", 1, border_color)
    screen.blit(label_garbage, (1080, 578))


def bottom_menu(screen, level, score, teleport, border_color):
    # poziom
    label_level = font2.render("Poziom: ", 1, border_color)
    screen.blit(label_level, (50, 710))

    label_level_int = font2.render(str(level), 1, border_color)
    screen.blit(label_level_int, (145, 711))

    # punkty
    label_score = font2.render("Punkty: ", 1, border_color)
    screen.blit(label_score, (300, 710))

    label_score_int = font2.render(str(score), 1, border_color)
    screen.blit(label_score_int, (390, 711))

    # teleporty
    label_teleport = font2.render("Bezpieczne teleporty: ", 1, border_color)
    screen.blit(label_teleport, (600, 710))

    label_teleport_int = font2.render(str(teleport), 1, border_color)
    screen.blit(label_teleport_int, (849, 711))


font = pygame.font.SysFont("calibri", 40)
font2 = pygame.font.SysFont("calibri", 28)
font3 = pygame.font.SysFont("calibri", 22)
font4 = pygame.font.SysFont("calibri", 72, 1)
