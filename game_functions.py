import stddraw
import pygame
import random
import sys

def detect_hit(pillars, pos_y, game_start):
    for i in range(len(pillars)):
        #Right X
        if 0.25 > pillars[i][0] and 0.25 < pillars[i][0] + .11:
            if i == 0 or i == 2:
                if pos_y[0] - 0.05 < pillars[i][2]:
                    game_start[0] = False
            if i == 1 or i == 3:
                if pos_y[0] + 0.05 > 1 - pillars[i][2]:
                    game_start[0] = False
            if i == 0 or i == 2:
                if pos_y[0] - 0.05 < pillars[i][2]:
                    game_start[0] = False
            if i == 1 or i == 3:
                if pos_y[0] + 0.05 > 1 - pillars[i][2]:
                    game_start[0] = False

def update_pillars(pillars):
    for i in range(len(pillars)):
        stddraw.filledRectangle(pillars[i][0], pillars[i][1], .10, pillars[i][2])
        pillars[i][0] = pillars[i][0] - .004

        if pillars[i][0] < -0.2:
            pillars[i][0] = 1.1
            #Set new heights for first set
            if i == 0:
                pillars[0][2] = random.uniform(0.1, 0.6)
            if i == 1:
                pillars[1][2] = .65 - pillars[0][2]
                pillars[1][1] = 1.0 - pillars[1][2]
            #Set new heights for second set
            if i == 2:
                pillars[2][2] = random.uniform(0.1, 0.6)
            if i == 3:
                pillars[3][2] = .65 - pillars[2][2]
                pillars[3][1] = 1.0 - pillars[3][2]

def restart_game(pillars, score, game_start):
        for i in range(len(pillars)):
            if i == 0 or i == 1:
                pillars[i][0] = 1.1
            if i == 2 or i == 3:
                pillars[i][0] = 1.7
        score[0] = 0
        game_start[0] = True


def update_player(pos_y, vel_y, gravity):
    pos_y[0] = pos_y[0] - vel_y[0]
    vel_y[0] = vel_y[0] + gravity
    if pos_y[0] < 0.05:
        pos_y[0] = 0.05
    if pos_y[0] > 1.04:
        pos_y[0] = 1.04
    if stddraw.mousePressed():
        vel_y[0] = -0.016

def update_score(pillars, score, high_score):
    for i in range(len(pillars)):
        if 0.25 > pillars[i][0] + .11 and 0.25 < pillars[i][0] + .111:
            score[0] = score[0] + 0.5
        if score[0] > high_score[0]:
            high_score[0] = score[0]

def main_menu_background(high_score, score):
    stddraw.setFontSize(80)
    stddraw.setPenColor(stddraw.LIGHT_GRAY)
    stddraw.text(0.5, 0.82, 'Flappy Box')
    stddraw.setFontSize(20)
    stddraw.text(.79, .1, 'high score =')
    stddraw.text(.9, .1, str(int(high_score[0])))
    stddraw.text(.2, .1, 'last score =')
    stddraw.text(.31, .1, str(int(score[0])))

def update_buttons(pillars, score, game_start, player_color, d):
    x, y = pygame.mouse.get_pos()
    if int(x) > 150 and int(x) < 210 and int(y) > 215 and int(y) < 245:
        stddraw.setFontSize(50)
        stddraw.setPenColor(stddraw.GRAY)
        stddraw.text(0.35, 0.55, 'Play')
        if stddraw.mousePressed():
            restart_game(pillars, score, game_start)
    else:
        stddraw.setFontSize(40)
        stddraw.setPenColor(stddraw.LIGHT_GRAY)
        stddraw.text(0.35, 0.55, 'Play')
    if int(x) > 305 and int(x) < 360 and int(y) > 215 and int(y) < 245:
        stddraw.setFontSize(50)
        stddraw.setPenColor(stddraw.LIGHT_GRAY)
        stddraw.text(0.65, 0.55, 'Exit')
        if stddraw.mousePressed():
            sys.exit()
    else:
        stddraw.setFontSize(40)
        stddraw.setPenColor(stddraw.LIGHT_GRAY)
        stddraw.text(0.65, 0.55, 'Exit')
    if int(x) > 230 and int(x) < 280 and int(y) > 280 and int(y) < 330:
        stddraw.setPenColor(player_color[d[0]])
        stddraw.filledSquare(.5, .4, .06)
        if stddraw.mousePressed():
            if d[0] != len(player_color) - 1:
                d[0] = d[0] + 1
            else:
                d[0] = 0
    else:
        stddraw.setPenColor(player_color[d[0]])
        stddraw.filledSquare(.5, .4, .05)


