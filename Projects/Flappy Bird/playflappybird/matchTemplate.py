# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:54:22 2020

@author: Owner
"""

import cv2

def matchTemplate(im, template, method):

    res = cv2.matchTemplate(im, template, eval(method))

    """
    """

    return res, im  