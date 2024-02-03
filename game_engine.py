import random
import pygame
from math import sqrt


def draw_enemy_position(player_pos, player_size):
    enemy_position = [random.randrange(20, 1020, player_size), random.randrange(20, 680, player_size)]
    if distance_from_enemy(player_pos, enemy_position) < 200:
        return draw_enemy_position(player_pos, player_size)
    return enemy_position


def add_enemies_to_list(enemy_list, do_create_enemies, number_of_enemies, player_pos, player_size):
    if do_create_enemies:
        while len(enemy_list) < number_of_enemies:
            enemy_position = draw_enemy_position(player_pos, player_size)
            if enemy_position == player_pos:
                add_enemies_to_list(enemy_list, do_create_enemies, number_of_enemies, player_pos, player_size)
            else:
                enemy_list.append(enemy_position)
    return False


def create_enemies(enemy_list, screen, enemy_color, enemy_size):
    for enemy in enemy_list:
        pygame.draw.rect(screen, enemy_color, (enemy[0], enemy[1], enemy_size, enemy_size))


def move_enemies(enemy_list, player_pos, enemy_size):
    for enemy in enemy_list:
        if enemy[0] < player_pos[0] and enemy[1] < player_pos[1]:
            enemy[0] += enemy_size
            enemy[1] += enemy_size

        elif enemy[0] > player_pos[0] and enemy[1] > player_pos[1]:
            enemy[0] -= enemy_size
            enemy[1] -= enemy_size

        elif enemy[0] < player_pos[0] and enemy[1] > player_pos[1]:
            enemy[0] += enemy_size
            enemy[1] -= enemy_size

        elif enemy[0] > player_pos[0] and enemy[1] < player_pos[1]:
            enemy[0] -= enemy_size
            enemy[1] += enemy_size

        elif enemy[1] == player_pos[1]:
            if enemy[0] > player_pos[0]:
                enemy[0] -= enemy_size
            else:
                enemy[0] += enemy_size

        elif enemy[0] == player_pos[0]:
            if enemy[1] > player_pos[1]:
                enemy[1] -= enemy_size
            else:
                enemy[1] += enemy_size


def detect_collision_with_player(enemy_pos, player_pos):
    if enemy_pos[0] == player_pos[0] and enemy_pos[1] == player_pos[1]:
        return True


def enemy_collision_with_player(enemy_list, player_pos):
    for enemy in enemy_list:
        if detect_collision_with_player(enemy, player_pos):
            return True
    return False


def detect_collision_enemies(enemy_list):
    collision_coord = []
    indexes_to_remove = []
    for index, enemy in enumerate(enemy_list):
        for enemy2 in range(index, len(enemy_list)):
            if index != enemy2:
                if enemy[0] == enemy_list[enemy2][0] and enemy[1] == enemy_list[enemy2][1]:
                    if [enemy[0], enemy[1]] not in collision_coord:
                        collision_coord.append([enemy[0], enemy[1]])
                    if index not in indexes_to_remove:
                        indexes_to_remove.append(index)
                    if enemy2 not in indexes_to_remove:
                        indexes_to_remove.append(enemy2)
    indexes_to_remove.sort(reverse=True)

    return collision_coord, indexes_to_remove


def destroy_enemies(enemy_list):
    collision_cord, indexes_to_remove = detect_collision_enemies(enemy_list)

    for idx in indexes_to_remove:
        enemy_list.pop(idx)
        return True


def update_garbage_list(enemy_list, garbage_list):
    collision_cord, indexes_to_remove = detect_collision_enemies(enemy_list)

    for pos in collision_cord:
        if pos not in garbage_list:
            garbage_list.append([pos[0], pos[1]])


def make_garbage_pill(garbage_list, screen, garbage_color, garbage_size):
    for garbage in garbage_list:
        pygame.draw.rect(screen, garbage_color, (garbage[0], garbage[1], garbage_size, garbage_size))


def detect_enemy_collision_with_garbage(enemy_list, garbage_list):
    for index, enemy in enumerate(enemy_list):
        for garbage in garbage_list:
            if enemy[0] == garbage[0] and enemy[1] == garbage[1]:
                enemy_list.pop(index)
                return True


def detect_player_collision_with_garbage(player_pos, garbage_list):
    for garbage in garbage_list:
        if garbage[0] == player_pos[0] and garbage[1] == player_pos[1]:
            return True
    return False


def distance_from_enemy(player_pos, enemy_pos):
    distance = sqrt((enemy_pos[0] - player_pos[0]) * (enemy_pos[0] - player_pos[0])
                    + (enemy_pos[1] - player_pos[1]) * (enemy_pos[1] - player_pos[1]))
    return distance


def safe_teleport(player_pos, enemy_list, player_size, garbage_list):
    x = random.randrange(20, 1020, player_size)
    y = random.randrange(20, 680, player_size)

    telep_coord = [x, y]
    for garbage in garbage_list:
        if x == garbage[0] and y == garbage[1]:
            telep_coord = safe_teleport(player_pos, enemy_list, player_size, garbage_list)
            break

    for enemy in enemy_list:
        if distance_from_enemy(telep_coord, enemy) < 120:
            telep_coord = safe_teleport(player_pos, enemy_list, player_size, garbage_list)
            break

    return telep_coord[0], telep_coord[1]


def add_teleport(score, req_points):
    if score >= req_points:
        return True
