# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:37:33 2020

@author: Owner
"""
import sys
sys.path.append("game/")
import cv2
import wrapped_flappy_bird as game

game_state = game.GameState()

init = [1, 0]

im, _, _ = game_state.frame_step(init)

bird = cv2.imread('assets/sprites/redbird-midflap.png')

pipe = cv2.imread('assets/sprites/pipe-green.png')

pipe = pipe[:50,:,:]


def matchTemplate(im, template, mode=cv2.TM_CCOEFF):


    res = cv2.matchTemplate(im, template, cv2.TM_CCOEFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val > 1e7:

        left, top = max_loc

        right, bottom = left + template.shape[1], top + template.shape[0]

        return left, top, right, bottom
    return None

find_pipe = False

while True:

    action = [1, 0]

    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)


    bird_left, bird_top, bird_right, bird_bottom = matchTemplate(im, bird)
    cv2.rectangle(im, (bird_left, bird_top), (bird_right, bird_bottom), 255, 2)

    if find_pipe:

        im = im[:,:pipe_right,:]
        pipe_left, pipe_top, pipe_right, pipe_bottom = matchTemplate(im, pipe)                
        action = [0, 1] if pipe_top < bird_bottom + 10 else [1, 0]

        if bird_left > pipe_right:
            find_pipe = False

    else:
        result = matchTemplate(im, pipe)

        if result:

            pipe_left, pipe_top, pipe_right, pipe_bottom = result

            action = [0, 1] if pipe_top < bird_bottom + 10 else [1, 0]

            find_pipe = True

    if find_pipe:
        cv2.rectangle(im, (pipe_left, pipe_top), (pipe_right, pipe_bottom), 0, 2)

    cv2.imshow('im', im)

    cv2.waitKey(1)

    im, _, t = game_state.frame_step(action)

    if t:

        cv2.waitKey(0) 
        break