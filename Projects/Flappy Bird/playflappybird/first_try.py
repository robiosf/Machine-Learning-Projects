# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:25:32 2020

@author: Zhizheng.Wang
"""

import sys
sys.path.append("game/")
import cv2
import wrapped_flappy_bird as game

game_state = game.GameState()
do = [0, 1]
image, reward, terminal = game_state.frame_step(do)
print (image.shape, reward, terminal)

image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow('image', image)
cv2.waitKey(0)