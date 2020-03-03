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
# 创建实例
do = [0, 1]
image, reward, terminal = game_state.frame_step(do)
# 将一个动作输入到游戏中，获得游戏返回的结果
print (image.shape, reward, terminal)
# 打印 image 的大小， reward 和 terminal 的值