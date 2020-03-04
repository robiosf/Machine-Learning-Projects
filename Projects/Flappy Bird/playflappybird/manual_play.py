# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:32:13 2020

@author: Owner
"""

import sys
sys.path.append("game/")
import wrapped_flappy_bird as game

game_state = game.GameState()


while True:

    do = [1, 0]
    image, reward, terminal = game_state.frame_step(do, manual=True)