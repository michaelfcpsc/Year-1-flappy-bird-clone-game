import stddraw
import pygame
import random
import game_functions as gf


#Player initial settings
pos_x = 0.2
pos_y = [0.5]
vel_y = [0]
gravity = 0.0008

#Pillars initial settings
    #pillar 1
bottom_height = random.uniform(0.2, 0.4)
top_height = .65 - bottom_height
top_start = 1.0 - top_height
    #pillar 2
bottom_height2 = random.uniform(0.2, 0.4)
top_height2 = .65 - bottom_height2
top_start2 = 1.0 - top_height2

#Pillar list
pillars = [[1.1, 0.0, bottom_height], [1.1, top_start, top_height], 
            [1.7, 0.0, bottom_height2], [1.7, top_start2, top_height2]]

#Player Color List
s = stddraw
player_color = [s.BLACK, s.BOOK_RED, s.GRAY, s.CYAN, s.VIOLET]
d = [0]

#Score count
score = [0]
high_score = [0]
game_start = [False]

while True:
    #Main Menu
    gf.main_menu_background(high_score, score)
    gf.update_buttons(pillars, score, game_start, player_color, d)
    if stddraw.mousePressed():
        print('')
    stddraw.show(11)
    stddraw.clear(stddraw.DARK_GRAY)
    while game_start[0]:
        #Draw score
        stddraw.setFontSize(300)
        stddraw.setPenColor(stddraw.GRAY)
        stddraw.text(0.5, 0.5, str(int(score[0])))

        #Update Player
        gf.update_player(pos_y, vel_y, gravity)
        stddraw.setPenColor(player_color[d[0]])
        stddraw.filledSquare(pos_x, pos_y[0], 0.05)

        #Load Pillar Objects
        stddraw.setPenColor(stddraw.LIGHT_GRAY)
        gf.update_pillars(pillars)

        # Hitboxes
        gf.detect_hit(pillars, pos_y, game_start)

        #Update score
        gf.update_score(pillars, score, high_score)

        stddraw.show(10)
        stddraw.clear(stddraw.DARK_GRAY)

